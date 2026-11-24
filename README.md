# AkbankPythonveYapayZekaBootcamp

## Metro Simulation

### 1. Project Description

This project aims to find the shortest route between metro stations and the route with the fewest transfers. The user selects a start and an end point and can find out the fastest route and the route with the fewest transfers.

### 2. Technologies and Libraries Used

 - **Python 3:** The main programming language of the project.

 - **collections:** Used for the `defaultdict` and `deque` structures.

 - **heapq:** Used to create the priority queue in the A* algorithm.

 - **typing:** Used for type hints.

### 3. How the Algorithms Work

#### BFS Algorithm (Route with Fewest Transfers)

The BFS algorithm is used to find the shortest path or the route with the fewest transfers by exploring a graph layer by layer. In this algorithm, all neighboring stations are explored in order starting from the starting point, and this continues until the target station is found. This way, the shortest path with the minimum number of transfers is found.

#### A* Algorithm (Fastest Route)
At each step, the A* algorithm finds the path with the lowest duration by taking into account the current path and the estimated distance to the target. This makes it possible to find faster routes. By prioritizing routes and calculating the total duration at each step, the A* algorithm finds the route that provides the shortest duration.

### Why Are These Algorithms Used?
- The **BFS** algorithm is very effective for finding the route with the fewest transfers because neighboring stations are explored at each level.
- The **A\*** algorithm, on the other hand, provides optimization between route lengths and durations and is preferred for finding faster routes.


### 4. Example Usage and Test Results

Some test scenarios were applied on the metro network given below.

#### Test 1: Route with fewest transfers and fastest route from AŞTİ to OSB

    `print("\n1. From AŞTİ to OSB:")`
    `route = metro.find_min_transfer_route("M1", "K4")`
    `if route:`
        `print("Route with fewest transfers:", " -> ".join(i.name for i in route))`

    `result = metro.find_fastest_route("M1", "K4")`
    `if result:`
        `route, duration = result`
        `print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))`

##### Output:

`1. From AŞTİ to OSB:`

`Route with fewest transfers: AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB`

`Fastest route (25 minutes): AŞTİ -> Kızılay -> Kızılay -> Ulus -> Demetevler -> OSB`

#### Test 2: Route with fewest transfers and fastest route from Batıkent to Keçiören

    `print("\n2. From Batıkent to Keçiören:")`
    `route = metro.find_min_transfer_route("T1", "T4")`
    `if route:`
        `print("Route with fewest transfers:", " -> ".join(i.name for i in route))`

    `result = metro.find_fastest_route("T1", "T4")`
    `if result:`
        `route, duration = result`
        `print(f"Fastest route ({duration} minutes):", " -> ".join(i.name for i in route))`

##### Output:

`2. From Batıkent to Keçiören:`

`Route with fewest transfers: Batıkent -> Demetevler -> Gar -> Keçiören`

`Fastest route (21 minutes): Batıkent -> Demetevler -> Gar -> Keçiören`

### 5. Ideas for Improving the Project

- **Error handling:** A structure could be added that checks for incorrect inputs and returns appropriate errors to the user.

- **Map integration:** A map interface that visualizes the metro stations could be developed.

- **Real-time data:** A system could be added that dynamically updates metro service times and waiting times.

- **Different optimizations:** Route suggestions could be offered based on different metrics (for example, ticket price or crowding).
