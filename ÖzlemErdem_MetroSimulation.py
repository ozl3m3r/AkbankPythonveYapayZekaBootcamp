from collections import defaultdict, deque # Koleksiyonlar modülünden özel veri yapıları içe aktarılır.
import heapq # Öncelik kuyruğu (min-heap) için heapq modülü kullanılır.
from typing import Dict, List, Set, Tuple, Optional # Tip ipuçları (type hints) için gerekli türler içe aktarılır.

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx # İstasyonun kimlik numarası (ID)
        self.ad = ad # İstasyonun adı
        self.hat = hat # İstasyonun ait olduğu hat
        self.komsular: List[Tuple['Istasyon', int]] = []  # (istasyon, süre) tuple'ları

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))  # Komşu istasyonu ve ulaşım süresini listeye ekler

class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {} # İstasyonların ID'ye göre saklandığı sözlük
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list) # Hat bazında istasyonları saklayan sözlük (default olarak boş liste oluşturur)

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:
        # Eğer istasyon ID daha önce eklenmemişse yeni bir istasyon oluşturur
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat)
            self.istasyonlar[idx] = istasyon # İstasyonu ID ile saklar
            self.hatlar[hat].append(istasyon) # İlgili hattın istasyon listesine ekler

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        # İstasyonları ID ile sözlükten al
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        # İki istasyonu birbirine bağla (çift yönlü bağlantı)
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        """BFS algoritması kullanarak en az aktarmalı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. BFS algoritmasını kullanarak en az aktarmalı rotayı bulun
        3. Rota bulunamazsa None, bulunursa istasyon listesi döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - collections.deque kullanarak bir kuyruk oluşturun, HINT: kuyruk = deque([(baslangic, [baslangic])])
        - Ziyaret edilen istasyonları takip edin
        - Her adımda komşu istasyonları keşfedin
        """

        # Eğer başlangıç veya hedef istasyon haritada yoksa, rota bulunamaz.
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        # Başlangıç ve hedef istasyon nesnelerini al.
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        ziyaret_edildi = {baslangic} # Ziyaret edilen istasyonları takip etmek için bir küme (set) oluştur.

        # BFS için kuyruk oluştur: (mevcut_istasyon, rota)
        # Başlangıçta kuyrukta sadece başlangıç istasyonu var
        kuyruk = deque()
        kuyruk.append((baslangic, [baslangic]))

        # Ziyaret edilen istasyonları takip etmek için küme
        ziyaret_edildi = set()
        ziyaret_edildi.add(baslangic)

        while kuyruk:
            # Kuyruğun başındaki elemanı al
            mevcut_durak, rota = kuyruk.popleft()

            # Hedefe ulaşıldıysa rotayı döndür
            if mevcut_durak == hedef:
                return rota

            # Mevcut istasyonun tüm komşularını kontrol et
            for komsu_durak, _ in mevcut_durak.komsular:
                # Eğer komşu daha önce ziyaret edilmediyse
                if komsu_durak not in ziyaret_edildi:
                    # Komşuyu ziyaret edildi olarak işaretle
                    ziyaret_edildi.add(komsu_durak)
                    # Yeni rotayı oluştur ve mevcut rotaya komşuyu ekle
                    yeni_rota = rota.copy()
                    yeni_rota.append(komsu_durak)
                    # Kuyruğa yeni rotayı ekle
                    kuyruk.append((komsu_durak, yeni_rota))

        # Rota bulunamadı
        return None

    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        """A* algoritması kullanarak en hızlı rotayı bulur

        Bu fonksiyonu tamamlayın:
        1. Başlangıç ve hedef istasyonların varlığını kontrol edin
        2. A* algoritmasını kullanarak en hızlı rotayı bulun
        3. Rota bulunamazsa None, bulunursa (istasyon_listesi, toplam_sure) tuple'ı döndürün
        4. Fonksiyonu tamamladıktan sonra, # TODO ve pass satırlarını kaldırın

        İpuçları:
        - heapq modülünü kullanarak bir öncelik kuyruğu oluşturun, HINT: pq = [(0, id(baslangic), baslangic, [baslangic])]
        - Ziyaret edilen istasyonları takip edin
        - Her adımda toplam süreyi hesaplayın
        - En düşük süreye sahip rotayı seçin
        """

        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            # Eğer başlangıç veya hedef istasyonları istasyonlar sözlüğünde bulunmuyorsa, rota bulunamaz.
            return None

        # Başlangıç istasyonunu, hedef istasyonunu sözlükten alıyoruz.
        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]
        # Ziyaret edilen istasyonları takip etmek için boş bir küme (set) oluşturuyoruz.
        # BFS algoritmasında her bir istasyonu yalnızca bir kez ziyaret etmemiz gerekiyor.
        ziyaret_edildi = set()

        # Öncelik kuyruğu (pq): (toplam_sure, id(mevcut_durak), mevcut_durak, rota)
        pq = []
        # Başlangıç noktası kuyruğa ekleniyor.
        heapq.heappush(pq, (0, id(baslangic), baslangic, [baslangic]))

        # Ziyaret edilen duraklar ve en kısa süreleri saklanacak.
        ziyaret_edildi = {}

        # Öncelik kuyruğu boşalana kadar devam et.
        while pq:
            # En düşük süreli öğeyi al.
            toplam_sure, _, mevcut_durak, rota = heapq.heappop(pq)

            # Eğer hedef durağa ulaşıldıysa, rota ve toplam süreyi döndür.
            if mevcut_durak == hedef:
                return (rota, toplam_sure)

            # Eğer bu istasyon daha önce daha düşük süreyle ziyaret edildiyse atla
            if mevcut_durak in ziyaret_edildi and ziyaret_edildi[mevcut_durak] < toplam_sure:
                continue

            # Tüm komşuları kontrol et
            for komsu_durak, sure in mevcut_durak.komsular:
                # Yeni toplam süreyi hesapla (mevcut süre + komşuya gidiş süresi)
                yeni_toplam = toplam_sure + sure
                # Eğer komşu ilk kez ziyaret ediliyor veya daha iyi bir yol bulunduysa
                if komsu_durak not in ziyaret_edildi or yeni_toplam < ziyaret_edildi.get(komsu_durak, float('inf')):
                    # Bu komşu için en iyi süreyi güncelle
                    ziyaret_edildi[komsu_durak] = yeni_toplam
                    # Yeni rotayı oluştur
                    yeni_rota = rota.copy()
                    yeni_rota.append(komsu_durak)
                    # Öncelik kuyruğuna yeni rotayı ekle
                    heapq.heappush(pq, (yeni_toplam, id(komsu_durak), komsu_durak, yeni_rota))

        # Rota bulunamadı
        return None

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()

    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")

    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")

    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")

    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB

    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar

    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören

    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma

    # Test senaryoları
    print("\n=== Test Senaryoları ===")

    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 4: Sıhhiye'den Keçiören'e (Mavi Hat'tan Turuncu Hat'a aktarma)
    print("\n4. Sıhhiye'den Keçiören'e:")
    rota = metro.en_az_aktarma_bul("M3", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("M3", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))

    # Senaryo 5: OSB'den Batıkent'e (Kırmızı Hat'tan Turuncu Hat'a aktarma)
    print("\n5. OSB'den Batıkent'e:")
    rota = metro.en_az_aktarma_bul("K4", "T1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))

    sonuc = metro.en_hizli_rota_bul("K4", "T1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))