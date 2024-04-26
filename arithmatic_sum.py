import random
from operator import add, sub, mul

# Define a simple representation of the problem
variables = {'a': 10, 'b': 5, 'c': 15, 'd': 2}
operations = [add, add] # Starting with addition as the primary operation for both solutions

# Target output
target = 30

# Generate initial population
def generate_population(size, variables):
    population = []
    for _ in range(size):
        individual = random.sample(list(variables.keys()), k=3)  # Convert keys to list
        population.append(individual)
    return population


# Fitness function
def evaluate(individual, variables):
    # Simplified evaluation: compute the sum of the selected variables
    result = sum(variables[var] for var in individual)
    fitness = abs(target - result)  # Lower is better
    return fitness

# Selection
def select(population, variables, k=5):
    scored_population = sorted((evaluate(individual, variables), individual) for individual in population)
    selected = [individual for _, individual in scored_population[:k]]
    return selected

# Crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, min(len(parent1), len(parent2)) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation
def mutate(individual, variables, mutation_rate=0.1):
    if random.random() < mutation_rate:
        mutation_point = random.randint(0, len(individual) - 1)
        individual[mutation_point] = random.choice(list(variables.keys()))
    return individual

# Evolutionary algorithm
def evolve(variables, generations=100, population_size=10):
    population = generate_population(population_size, variables)
    for generation in range(generations):
        selected = select(population, variables)
        next_generation = selected
        while len(next_generation) < population_size:
            parent1, parent2 = random.sample(selected, 2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, variables)
            child2 = mutate(child2, variables)
            next_generation += [child1, child2]
            print("code running")
        population = next_generation
        best_solution = min(population, key=lambda ind: evaluate(ind, variables))
        best_fitness = evaluate(best_solution, variables)
        if best_fitness == 0:  # Found a solution
            break
    return best_solution, best_fitness

# Run the evolutionary algorithm
best_solution, best_fitness = evolve(variables)
print(best_solution, best_fitness)
