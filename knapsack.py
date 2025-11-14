import random
import math


# Problem setup

Objects = {
    'A': (10, 2),
    'B': (6, 3),
    'C': (4, 8),
    'D': (8, 5),
    'E': (9, 5),
    'F': (7, 6)
}

Capacity = 15
Items = list(Objects.keys())  # ['A', 'B', 'C', 'D', 'E', 'F']
num_items = len(Items)



# Value function

def value(state):
    total_weight = 0
    total_value = 0

    for i in range(num_items):
        if state[i] == 1:
            item = Items[i]
            weight, val = Objects[item]
            total_weight += weight
            total_value += val

    # if overweight, invalid state
    if total_weight > Capacity:
        return -1  # illegal state
    else:
        return total_value



# Generate neighbor

def get_neighbor(state):
    new_state = state[:]
    i = random.randint(0, num_items - 1)
    # flip the bit
    new_state[i] = 1 - new_state[i]
    return new_state



# Simulated annealing algorithm

def simulated_annealing(initial_temp=100, cooling_rate=0.95, min_temp=1):
    # start from a random state
    current_state = [random.randint(0, 1) for _ in range(num_items)]
    current_value = value(current_state)

    best_state = current_state[:]
    best_value = current_value

    T = initial_temp

    while T > min_temp:
        neighbor = get_neighbor(current_state)
        neighbor_value = value(neighbor)

        # Only consider legal neighbors
        if neighbor_value != -1:
            delta = neighbor_value - current_value

            # if neighbor is better, accept it
            if delta > 0:
                current_state = neighbor
                current_value = neighbor_value
            else:
                # if neighbor is worse, accept it with some probability
                prob = math.exp(delta / T)
                if random.random() < prob:
                    current_state = neighbor
                    current_value = neighbor_value

            # update the best state found so far
            if current_value > best_value:
                best_value = current_value
                best_state = current_state[:]

        # cool down
        T = T * cooling_rate

    return best_state, best_value



# Main program

if __name__ == "__main__":
    best_state, best_value = simulated_annealing()

    print("\nBest solution found:")
    print(f"Selected items: {[Items[i] for i in range(num_items) if best_state[i] == 1]}")
    print(f"Best value: {best_value}")
    total_weight = sum(
        Objects[Items[i]][0] for i in range(num_items) if best_state[i] == 1
    )
    print(f"Total weight: {total_weight}")
