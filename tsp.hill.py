import random

# define the distance between cities
tsp = [
    [0, 400, 500, 300],
    [400, 0, 300, 500],
    [500, 300, 0, 400],
    [300, 500, 400, 0]
]

cities = len(tsp)  # number of cities


# Value function: compute total distance of a route

def value(state):
    total_distance = 0
    for i in range(len(state) - 1):
        total_distance += tsp[state[i]][state[i + 1]]
    # Add distance back to start
    total_distance += tsp[state[-1]][state[0]]
    return total_distance



# Generate a neighbor by swapping two random cities (not the starting city)

def get_neighbor(state):
    new_state = state[:]
    # Choose two random cities to swap (excluding city 0 if you want it fixed as the start)
    i, j = random.sample(range(1, len(state)), 2)
    new_state[i], new_state[j] = new_state[j], new_state[i]
    return new_state



# Hill climbing algorithm

def hill_climb(state):
    current = state
    current_value = value(current)

    while True:
        neighbor = get_neighbor(current)
        neighbor_value = value(neighbor)

        # If neighbor is better, move to it
        if neighbor_value < current_value:
            current = neighbor
            current_value = neighbor_value
        else:
            # No better neighbor found (local minimum)
            break
    return current, current_value



# Hill climbing with random restarts

def hill_climb_random_restart(max_restarts=10):
    best_state = None
    best_value = float('inf')

    for r in range(max_restarts):
        # Start from a random state (fix city 0 at start)
        state = list(range(cities))
        random.shuffle(state[1:])  # keep city 0 fixed
        state[0] = 0

        current, current_value = hill_climb(state)

        print(f"Restart {r+1}: Route {current} -> Distance {current_value}")

        if current_value < best_value:
            best_state = current
            best_value = current_value

    print("\nBest route found:")
    print(f"Route: {best_state} -> Distance: {best_value}")



# Run the algorithm

if __name__ == "__main__":
    random.seed()  # optional for reproducibility
    hill_climb_random_restart(max_restarts=10)

