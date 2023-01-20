import random
from Distance import calc_distance

def tabu_search(cities, tabu_list_size = 100, num_iterations = 1000):
  # Initialize solution with a random path
  solution = random.sample(cities, len(cities))
  
  # Calculate initial distance of solution
  distance = calc_distance(solution)
  
  # Set best solution to initial solution
  best_solution = solution
  best_distance = distance
  
  # Initialize tabu list
  tabu_list = []
  
  # Run tabu search
  for i in range(num_iterations):
    # Generate new solutions by swapping two cities
    new_solutions = []
    for j in range(len(cities)):
      new_solution = mutate(solution, j)
      new_solutions.append(new_solution)
    
    # Evaluate new solutions
    new_distances = []
    for new_solution in new_solutions:
      new_distance = calc_distance(new_solution)
      new_distances.append(new_distance)
    
    # Select best new solution
    min_index = min(range(len(new_distances)), key=new_distances.__getitem__)
    new_solution = new_solutions[min_index]
    new_distance = new_distances[min_index]
    
    # If new solution is better, accept it
    if new_distance < distance:
      solution = new_solution
      distance = new_distance
      
      # If new solution is better than the best solution, update best solution
      if new_distance < best_distance:
        best_solution = new_solution
        best_distance = new_distance
    
    # Add new solution to tabu list
    tabu_list.append(new_solution)
    if len(tabu_list) > tabu_list_size:
      tabu_list.pop(0)
  
  best_tour = []
  best_tour.append(best_solution)
  best_tour.append(best_distance)
  return best_tour

def mutate(individual, index):
  # Swap city at index with next city, if index is not the last index
  if index < len(individual) - 1:
    individual[index], individual[index+1] = individual[index+1], individual[index]
  return individual