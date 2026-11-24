from collections import defaultdict, deque # Imports special data structures from the collections module.
import heapq # The heapq module is used for the priority queue (min-heap).
from typing import Dict, List, Set, Tuple, Optional # Imports the types needed for type hints.

class Station:
    def __init__(self, idx: str, name: str, line: str):
        self.idx = idx # Station ID
        self.name = name # Station name
        self.line = line # Line the station belongs to
        self.neighbors: List[Tuple['Station', int]] = []  # (station, duration) tuples

    def add_neighbor(self, station: 'Station', duration: int):
        self.neighbors.append((station, duration))  # Adds the neighboring station and the travel time to the list

class MetroNetwork:
    def __init__(self):
        self.stations: Dict[str, Station] = {} # Dictionary that stores stations by ID
        self.lines: Dict[str, List[Station]] = defaultdict(list) # Dictionary that stores stations per line (creates an empty list by default)

    def add_station(self, idx: str, name: str, line: str) -> None:
        # Creates a new station if the station ID has not been added before
        if idx not in self.stations:
            station = Station(idx, name, line)
            self.stations[idx] = station # Stores the station by its ID
            self.lines[line].append(station) # Adds it to the station list of the relevant line

    def add_connection(self, station1_id: str, station2_id: str, duration: int) -> None:
        # Get the stations from the dictionary by ID
        station1 = self.stations[station1_id]
        station2 = self.stations[station2_id]
        # Connect the two stations to each other (bidirectional connection)
        station1.add_neighbor(station2, duration)
        station2.add_neighbor(station1, duration)

    def find_min_transfer_route(self, start_id: str, target_id: str) -> Optional[List[Station]]:
        """Finds the route with the fewest transfers using the BFS algorithm

        Complete this function:
        1. Check that the start and target stations exist
        2. Find the route with the fewest transfers using the BFS algorithm
        3. Return None if no route is found, otherwise return the list of stations
        4. After completing the function, remove the # TODO and pass lines

        Hints:
        - Create a queue using collections.deque, HINT: queue = deque([(start, [start])])
        - Keep track of visited stations
        - Explore neighboring stations at each step
        """

        # If the start or target station is not on the map, no route can be found.
        if start_id not in self.stations or target_id not in self.stations:
            return None
        # Get the start and target station objects.
        start = self.stations[start_id]
        target = self.stations[target_id]
        visited = {start} # Create a set to keep track of visited stations.

        # Create the queue for BFS: (current_station, route)
        # Initially the queue only contains the start station
        queue = deque()
        queue.append((start, [start]))

        # Set to keep track of visited stations
        visited = set()
        visited.add(start)

        while queue:
            # Take the element at the front of the queue
            current_station, route = queue.popleft()

            # If the target has been reached, return the route
            if current_station == target:
                return route

            # Check all neighbors of the current station
            for neighbor_station, _ in current_station.neighbors:
                # If the neighbor has not been visited before
                if neighbor_station not in visited:
                    # Mark the neighbor as visited
                    visited.add(neighbor_station)
                    # Build the new route by adding the neighbor to the current route
                    new_route = route.copy()
                    new_route.append(neighbor_station)
                    # Add the new route to the queue
                    queue.append((neighbor_station, new_route))

        # No route found
        return None

    def find_fastest_route(self, start_id: str, target_id: str) -> Optional[Tuple[List[Station], int]]:
        """Finds the fastest route using the A* algorithm

        Complete this function:
        1. Check that the start and target stations exist
        2. Find the fastest route using the A* algorithm
        3. Return None if no route is found, otherwise return a (station_list, total_duration) tuple
        4. After completing the function, remove the # TODO and pass lines

        Hints:
        - Create a priority queue using the heapq module, HINT: pq = [(0, id(start), start, [start])]
        - Keep track of visited stations
        - Calculate the total duration at each step
        - Choose the route with the lowest duration
        """

        if start_id not in self.stations or target_id not in self.stations:
            # If the start or target station is not in the stations dictionary, no route can be found.
            return None

        # Get the start station and the target station from the dictionary.
        start = self.stations[start_id]
        target = self.stations[target_id]
        # Create an empty set to keep track of visited stations.
        # In the BFS algorithm, each station only needs to be visited once.
        visited = set()

        # Priority queue (pq): (total_duration, id(current_station), current_station, route)
        pq = []
        # The starting point is added to the queue.
        heapq.heappush(pq, (0, id(start), start, [start]))

        # Visited stations and their shortest durations will be stored.
        visited = {}

        # Continue until the priority queue is empty.
        while pq:
            # Take the item with the lowest duration.
            total_duration, _, current_station, route = heapq.heappop(pq)

            # If the target station has been reached, return the route and the total duration.
            if current_station == target:
                return (route, total_duration)

            # Skip this station if it was previously visited with a lower duration
            if current_station in visited and visited[current_station] < total_duration:
                continue

            # Check all neighbors
            for neighbor_station, duration in current_station.neighbors:
                # Calculate the new total duration (current duration + travel time to the neighbor)
                new_total = total_duration + duration
                # If the neighbor is being visited for the first time or a better path has been found
                if neighbor_station not in visited or new_total < visited.get(neighbor_station, float('inf')):
                    # Update the best duration for this neighbor
                    visited[neighbor_station] = new_total
                    # Build the new route
                    new_route = route.copy()
                    new_route.append(neighbor_station)
                    # Add the new route to the priority queue
                    heapq.heappush(pq, (new_total, id(neighbor_station), neighbor_station, new_route))

        # No route found
        return None

# Example Usage
if __name__ == "__main__":
    metro = MetroNetwork()

    # Adding stations
    # Red Line
    metro.add_station("K1", "Kızılay", "Kırmızı Hat")
    metro.add_station("K2", "Ulus", "Kırmızı Hat")
    metro.add_station("K3", "Demetevler", "Kırmızı Hat")
    metro.add_station("K4", "OSB", "Kırmızı Hat")

    # Blue Line
    metro.add_station("M1", "AŞTİ", "Mavi Hat")
    metro.add_station("M2", "Kızılay", "Mavi Hat")  # Transfer point
    metro.add_station("M3", "Sıhhiye", "Mavi Hat")
    metro.add_station("M4", "Gar", "Mavi Hat")

    # Orange Line
    metro.add_station("T1", "Batıkent", "Turuncu Hat")
    metro.add_station("T2", "Demetevler", "Turuncu Hat")  # Transfer point
    metro.add_station("T3", "Gar", "Turuncu Hat")  # Transfer point
    metro.add_station("T4", "Keçiören", "Turuncu Hat")

    # Adding connections
    # Red Line connections
    metro.add_connection("K1", "K2", 4)  # Kızılay -> Ulus
    metro.add_connection("K2", "K3", 6)  # Ulus -> Demetevler
    metro.add_connection("K3", "K4", 8)  # Demetevler -> OSB

    # Blue Line connections
    metro.add_connection("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.add_connection("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.add_connection("M3", "M4", 4)  # Sıhhiye -> Gar

    # Orange Line connections
    metro.add_connection("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.add_connection("T2", "T3", 9)  # Demetevler -> Gar
    metro.add_connection("T3", "T4", 5)  # Gar -> Keçiören

    # Line transfer connections (same station on different lines)
    metro.add_connection("K1", "M2", 2)  # Kızılay transfer
    metro.add_connection("K3", "T2", 3)  # Demetevler transfer
    metro.add_connection("M4", "T3", 2)  # Gar transfer

    # Test scenarios
    print("\n=== Test Scenarios ===")

    # Scenario 1: From AŞTİ to OSB
    print("\n1. From AŞTİ to OSB:")
    route = metro.find_min_transfer_route("M1", "K4")
    if route:
        print("Route with fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("M1", "K4")
    if result:
        route, duration = result
        print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))

    # Scenario 2: From Batıkent to Keçiören
    print("\n2. From Batıkent to Keçiören:")
    route = metro.find_min_transfer_route("T1", "T4")
    if route:
        print("Route with fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("T1", "T4")
    if result:
        route, duration = result
        print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))

    # Scenario 3: From Keçiören to AŞTİ
    print("\n3. From Keçiören to AŞTİ:")
    route = metro.find_min_transfer_route("T4", "M1")
    if route:
        print("Route with fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("T4", "M1")
    if result:
        route, duration = result
        print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))

    # Scenario 4: From Sıhhiye to Keçiören (transfer from Blue Line to Orange Line)
    print("\n4. From Sıhhiye to Keçiören:")
    route = metro.find_min_transfer_route("M3", "T4")
    if route:
        print("Route with fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("M3", "T4")
    if result:
        route, duration = result
        print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))

    # Scenario 5: From OSB to Batıkent (transfer from Red Line to Orange Line)
    print("\n5. From OSB to Batıkent:")
    route = metro.find_min_transfer_route("K4", "T1")
    if route:
        print("Route with fewest transfers:", " -> ".join(i.name for i in route))

    result = metro.find_fastest_route("K4", "T1")
    if result:
        route, duration = result
        print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))
