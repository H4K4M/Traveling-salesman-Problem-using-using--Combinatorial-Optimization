import random
import math
from Distance import calc_distance

def simulated_annealing(cities, temperature = 1000, cooling_rate = 0.001, num_iterations = 1000):
  # Initialize solution with a random path
  solution = random.sample(cities, len(cities))
  
  # Calculate initial distance of solution
  distance = calc_distance(solution)
  
  # Set best solution to initial solution
  best_solution = solution
  best_distance = distance
  
  # Run simulated annealing
  for i in range(num_iterations):
    # Generate new solution by swapping two cities
    new_solution = mutate(solution)
    
    # Calculate new distance of solution
    new_distance = calc_distance(new_solution)
    
    # Calculate delta
    delta = new_distance - distance
    
    # If new solution is better, accept it
    if delta < 0:
      solution = new_solution
      distance = new_distance
      
      # If new solution is better than the best solution, update best solution
      if new_distance < best_distance:
        best_solution = new_solution
        best_distance = new_distance
    else:
      # Accept new solution with probability of e^(-delta/T)
      p = math.exp(-delta/temperature)
      if random.uniform(0, 1) < p:
        solution = new_solution
        distance = new_distance
    
    # Cool temperature
    temperature *= 1 - cooling_rate
  
  best_tour = []
  best_tour.append(best_solution)
  best_tour.append(best_distance)

  #return shortest path
  return best_tour

def mutate(individual):
  # Select two random cities and swap them
  city1 = random.randint(0, len(individual) - 1)
  city2 = random.randint(0, len(individual) - 1)
  individual[city1], individual[city2] = individual[city2], individual[city1]
  return individual