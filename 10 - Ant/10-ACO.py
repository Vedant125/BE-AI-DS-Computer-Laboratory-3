import numpy as np

# Parameters
num_cities = 5
num_ants = 50
num_iterations = 300
alpha = 1
beta = 2
evaporation_rate = 0.1

# Your fixed 5x5 distance matrix
distance_matrix = np.array([
    [0, 2, 2, 5, 7],
    [2, 0, 4, 8, 2],
    [2, 4, 0, 1, 3],
    [5, 8, 1, 0, 2],
    [7, 2, 3, 2, 0]
], dtype=float)

# Replace diagonal with infinity to avoid self-loops
np.fill_diagonal(distance_matrix, np.inf)

# Initialize pheromone matrix
pheromone_matrix = np.ones((num_cities, num_cities))

best_tour = None
best_tour_length = np.inf

for iteration in range(num_iterations):
    all_tours = []
    all_tour_lengths = []

    for ant in range(num_ants):
        tour = []
        visited = set()
        current_city = np.random.randint(0, num_cities)
        tour.append(current_city)
        visited.add(current_city)

        while len(visited) < num_cities:
            probabilities = []
            for city in range(num_cities):
                if city in visited:
                    probabilities.append(0)
                else:
                    pheromone = pheromone_matrix[current_city][city] ** alpha
                    heuristic = (1 / distance_matrix[current_city][city]) ** beta
                    probabilities.append(pheromone * heuristic)

            probabilities = np.array(probabilities)
            if probabilities.sum() == 0:
                # fallback in case all probabilities are zero
                unvisited = list(set(range(num_cities)) - visited)
                next_city = np.random.choice(unvisited)
            else:
                probabilities /= probabilities.sum()
                next_city = np.random.choice(range(num_cities), p=probabilities)

            tour.append(next_city)
            visited.add(next_city)
            current_city = next_city

        # Return to start city to complete the cycle
        tour.append(tour[0])
        tour_length = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(num_cities))
        all_tours.append(tour)
        all_tour_lengths.append(tour_length)

        # Update best tour
        if tour_length < best_tour_length:
            best_tour_length = tour_length
            best_tour = tour.copy()

    # Evaporate pheromones
    pheromone_matrix *= (1 - evaporation_rate)

    # Update pheromones based on all ant tours
    for i, tour in enumerate(all_tours):
        for j in range(num_cities):
            from_city = tour[j]
            to_city = tour[j + 1]
            pheromone_matrix[from_city][to_city] += 1 / all_tour_lengths[i]
            pheromone_matrix[to_city][from_city] += 1 / all_tour_lengths[i]  # symmetric update

print("Best tour:", best_tour)
print("Best tour length:", best_tour_length)
