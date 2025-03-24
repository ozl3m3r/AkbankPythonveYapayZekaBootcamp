# AkbankPythonveYapayZekaBootcamp

## Metro Simulation

### 1. Proje Açıklaması

Bu proje, metro istasyonları arasındaki en kısa rotayı ve en az aktarma ile gidilebilecek güzergahı bulmayı amaçlamaktadır. Kullanıcı, başlangıç ve bitiş noktalarını seçerek en hızlı rotayı ve en az aktarmalı rotayı öğrenebilir.

### 2. Kullanılan Teknolojiler ve Kütüphaneler

 - **Python 3:** Projenin temel programlama dilidir.

 - **collections:** `defaultdict` ve `deque` yapıları için kullanılmıştır.

 - **heapq:** A* algoritmasında öncelik kuyruğu oluşturmak için kullanılmıştır.

 - **typing:** Tür ipuçları için kullanılmıştır.

### 3. Algoritmaların Çalışma Mantığı

#### BFS Algoritması (En Az Aktarmalı Rota)

BFS algoritması, bir grafiği katman katman keşfederek en kısa yol veya en az aktarmalı rotayı bulmak için kullanılır. Bu algoritmada, başlangıç noktasından itibaren tüm komşu istasyonlar sırasıyla keşfedilir ve hedef istasyon bulunana kadar devam edilir. Bu sayede, minimum aktarma sayısı ile en kısa yol bulunur.

#### A* Algoritması (En Hızlı Rota)
A* algoritması, her adımda, mevcut yolu ve hedefe olan tahmini mesafeyi dikkate alarak, en düşük süreli yolu bulur. Bu sayede, daha hızlı rotalar bulunabilir. A* algoritması, rotaları öncelik sırasına koyarak ve her adımda toplam süreyi hesaplayarak, en kısa süreyi sağlayan rotayı bulur.

### Neden Bu Algoritmalar Kullanılıyor?
- **BFS** algoritması, en az aktarma ile rotayı bulmak için oldukça etkilidir çünkü her seviyede komşu istasyonlar keşfedilir.
- **A\*** algoritması ise, rota uzunlukları ve süreleri arasında optimizasyon sağlar, daha hızlı rotaları bulmak için tercih edilir.


### 4. Örnek Kullanım ve Test Sonuçları

Aşağıda verilen metro ağı üzerinden bazı test senaryoları uygulanmıştır.

#### Test 1: AŞTİ'den OSB'ye en az aktarmalı rota ve en hızlı rota

    `print("\n1. AŞTİ'den OSB'ye:")`
    `rota = metro.en_az_aktarma_bul("M1", "K4")`
    `if rota:`
        `print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))`

    `sonuc = metro.en_hizli_rota_bul("M1", "K4")`
    `if sonuc:`
        `rota, sure = sonuc`
        `print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))`

##### Çıktı:

`1. AŞTİ'den OSB'ye:`

`En az aktarmalı rota: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB`

`En hızlı rota (25 dakika): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB`

#### Test 2: Batıkent'ten Keçiören'e en az aktarmalı rota ve en hızlı rota

    `print("\n2. Batıkent'ten Keçiören'e:")`
    `rota = metro.en_az_aktarma_bul("T1", "T4")`
    `if rota:`
        `print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))`

    `sonuc = metro.en_hizli_rota_bul("T1", "T4")`
    `if sonuc:`
        `rota, sure = sonuc`
        `print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))`

##### Çıktı:

`2. Batıkent'ten Keçiören'e:`

`En az aktarmalı rota: Batıkent -> Demetevler -> Gar -> Keçiören`

`En hızlı rota (21 dakika): Batıkent -> Demetevler -> Gar -> Keçiören`

### 5. Projeyi Geliştirme Fikirleri

- **Hata yönetimi:** Yanlış girişleri kontrol eden ve kullanıcıya uygun hatalar döndüren bir yapı eklenebilir.

- **Harita entegrasyonu:** Metro istasyonlarını görselleştiren bir harita arayüzü geliştirilebilir.

- **Gerçek zamanlı veri:** Metro sefer sürelerini ve bekleme zamanlarını dinamik olarak güncelleyen bir sistem eklenebilir.

- **Farklı optimizasyonlar:** Farklı metriklere göre (örneğin bilet fiyatı veya kalabalık durumu) rota önerileri sunulabilir.
  

