import random
from Distance import calc_distance

def hill_climbing(cities, num_iterations = 1000):
  # Initialize solution with a random path
  solution = random.sample(cities, len(cities))
  
  # Calculate initial distance of solution
  distance = calc_distance(solution)
  
  # Set best solution to initial solution
  best_solution = solution
  best_distance = distance
  
  # Run hill climbing
  for i in range(num_iterations):
    # Generate new solution by swapping two cities
    new_solution = mutate(solution)
    
    # Calculate new distance of solution
    new_distance = calc_distance(new_solution)
    
    # If new solution is better, accept it
    if new_distance < distance:
      solution = new_solution
      distance = new_distance
      
      # If new solution is better than the best solution, update best solution
      if new_distance < best_distance:
        best_solution = new_solution
        best_distance = new_distance
  best_tour = []
  best_tour.append(best_solution)
  best_tour.append(best_distance)
  return best_tour
  

def mutate(individual):
  # Select two random cities and swap them
  city1 = random.randint(0, len(individual) - 1)
  city2 = random.randint(0, len(individual) - 1)
  individual[city1], individual[city2] = individual[city2], individual[city1]
  return individual