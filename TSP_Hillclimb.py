import random
import math

# Calculate the total distance of the tour
def total_distance(tour, distances):
    distance = 0
    for i in range(len(tour)):
        distance += distances[tour[i-1]][tour[i]]
    return distance

# Generate a random tour
def random_tour(cities):
    tour = list(cities)
    random.shuffle(tour)
    return tour

# Swap two cities in the tour
def swap_cities(tour):
    new_tour = list(tour)
    i, j = random.sample(range(len(tour)), 2)
    new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
    return new_tour

# Hill Climbing algorithm for TSP
def hill_climbing(cities, distances):
    current_tour = random_tour(cities)
    current_distance = total_distance(current_tour, distances)
    
    while True:
        new_tour = swap_cities(current_tour)
        new_distance = total_distance(new_tour, distances)
        
        if new_distance < current_distance:
            current_tour = new_tour
            current_distance = new_distance
        else:
            break

    return current_tour, current_distance

# Driver code
if __name__ == "__main__":
    # Number of cities
    cities = [0, 1, 2, 3, 4]

    # Distance matrix (symmetric)
    distances = [
        [0, 2, 9, 10, 7],
        [2, 0, 6, 4, 3],
        [9, 6, 0, 8, 5],
        [10, 4, 8, 0, 1],
        [7, 3, 5, 1, 0]
    ]

    # Solve the TSP using Hill Climbing
    best_tour, best_distance = hill_climbing(cities, distances)
    
    print("Best tour:", best_tour)
    print("Best distance:", best_distance)