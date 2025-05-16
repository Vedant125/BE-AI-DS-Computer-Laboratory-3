import numpy as np

class ClonalSelectionAlgorithm:
    def __init__(self, population_size, mutation_rate, generations, target_function):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.generations = generations
        self.target_function = target_function
        self.population = self.initialize_population()

    # Initialize the population with random antibodies
    def initialize_population(self):
        return np.random.uniform(-5, 5, (self.population_size, 2))  # 2D problem

    # Evaluate the fitness of each antibody
    def fitness(self, antibodies):
        return np.array([self.target_function(antibody) for antibody in antibodies])

    # Clonal Selection: Select the best antibodies based on fitness
    def select_best_antibodies(self, antibodies, fitness_values, n_best):
        best_indices = np.argsort(fitness_values)[:n_best]
        return antibodies[best_indices]

    # Mutation: Apply mutation to generate clones of the selected antibodies
    def mutate(self, antibodies):
        mutation = np.random.normal(0, self.mutation_rate, antibodies.shape)
        return antibodies + mutation

    # Run the Clonal Selection Algorithm
    def run(self):
        for generation in range(self.generations):
            fitness_values = self.fitness(self.population)
            best_antibodies = self.select_best_antibodies(self.population, fitness_values, n_best=self.population_size // 2)
            clones = self.mutate(best_antibodies)
            
            # Replace the worst half of the population with the new clones
            worst_indices = np.argsort(fitness_values)[self.population_size // 2:]
            self.population[worst_indices] = clones

            # Print the best solution in each generation
            print(f"Generation {generation+1}, Best Fitness: {min(fitness_values)}")

        # Return the best solution after all generations
        return self.population[np.argmin(fitness_values)]


# Example target function: Sphere function (simple 2D optimization problem)
def sphere_function(x):
    return np.sum(x**2)

# Example usage of CSA
if __name__ == "__main__":
    csa = ClonalSelectionAlgorithm(population_size=50, mutation_rate=0.1, generations=100, target_function=sphere_function)
    best_solution = csa.run()
    print(f"Best solution found: {best_solution}")
