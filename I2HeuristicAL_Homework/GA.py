import random
from Distance import calc_distance

def genetic_algorithm(cities, pop_size = 500, mutation_rate = 0.01, num_generations = 1000):
  # Initialize population
  population = []
  for i in range(pop_size):
    population.append(random.sample(cities, len(cities)))
  
  # Evaluate initial population
  population_fitness = []
  for individual in population:
    distance = calc_distance(individual)
    population_fitness.append((individual, distance))
  
  # Sort population by fitness
  population_fitness.sort(key=lambda x: x[1])
  
  # Run GA
  for i in range(num_generations):
    # Select parents
    parents = selection(population_fitness, pop_size)
    
    # Generate offspring
    offspring = crossover(parents, pop_size)
    
    # Mutate offspring
    offspring = mutation(offspring, mutation_rate)
    
    # Evaluate offspring
    offspring_fitness = []
    for individual in offspring:
      distance = calc_distance(individual)
      offspring_fitness.append((individual, distance))
    
    # Select next generation
    population_fitness = selection(offspring_fitness + population_fitness, pop_size)
  
  # Sort population by fitness
  population_fitness.sort(key=lambda x: x[1])
  
  #Return shortest path
  return population_fitness

def selection(population, pop_size):
  # Select individuals with higher fitness for reproduction
  return population[:pop_size//2]

def crossover(parents, pop_size):
  offspring = []
  for i in range(pop_size):
    # Select two random parents
    parent1 = random.choice(parents)
    parent2 = random.choice(parents)
    
    # Crossover parents to create offspring
    offspring.append(crossover_helper(parent1[0], parent2[0]))
  return offspring

def crossover_helper(parent1, parent2):
  # Select random index for crossover point
  crossover_point = random.randint(1, len(parent1) - 1)
  
  # Create offspring by combining parts of both parents
  offspring = parent1[:crossover_point]
  for city in parent2:
    if city not in offspring:
      offspring.append(city)
  return offspring

def mutation(offspring, mutation_rate):
  for i in range(len(offspring)):
    # Mutate offspring with probability of mutation rate
    if random.uniform(0, 1) < mutation_rate:
      offspring[i] = mutate(offspring[i])
  return offspring

def mutate(individual):
  # Select two random cities and swap them
  city1 = random.randint(0, len(individual) - 1)
  city2 = random.randint(0, len(individual) - 1)
  individual[city1], individual[city2] = individual[city2], individual[city1]
  return individual