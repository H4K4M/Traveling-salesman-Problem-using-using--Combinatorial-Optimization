import random
import math

def aco(cities, num_ants=100, num_iterations=1000, alpha=1, beta=2, rho=0.5):
  # Initialize pheromone matrix
  pheromone_matrix = [[1 / len(cities) for j in range(len(cities))] for i in range(len(cities))]
  
  # Initialize best solution to None
  best_solution = None
  best_distance = float("inf")
  
  # Run ACO
  for i in range(num_iterations):
    # Initialize solutions for each ant
    solutions = []
    distances = []
    
    # Generate solutions for each ant
    for j in range(num_ants):
      solution, distance = generate_solution(cities, pheromone_matrix, alpha, beta)
      solutions.append(solution)
      distances.append(distance)
      
      # Update best solution
      if distance < best_distance:
        best_solution = solution
        best_distance = distance
    
    # Update pheromone matrix
    pheromone_matrix = update_pheromones(pheromone_matrix, solutions, distances, rho)
  
  # Display final path and shortest path
  best_solution = [cities[i] for i in best_solution]
  # print("Final path:", best_solution)
  # print("Shortest path distance:", best_distance)
  best_tour = []
  best_tour.append(best_solution)
  best_tour.append(best_distance)
  return best_tour

def generate_solution(cities, pheromone_matrix, alpha, beta):
  # Initialize solution with first city
  solution = [0]
  
  # Generate solution by selecting next city based on pheromones and heuristics
  while len(solution) < len(cities):
    next_city = select_next_city(cities, solution, pheromone_matrix, alpha, beta)
    solution.append(next_city)
    # Calculate distance of solution
  distance = calc_distance(cities,solution)
  
  return solution, distance

def select_next_city(cities, solution, pheromone_matrix, alpha, beta):
  # Calculate selection probabilities for each city
  selection_probs = [0 for i in range(len(cities))]
  for i in range(len(cities)):
    if i not in solution:
      pheromone = pheromone_matrix[solution[-1]][i]
      heuristic = get_heuristic(cities[solution[-1]], cities[i])
      selection_probs[i] = (pheromone**alpha) * (heuristic**beta)
  
  # Normalize selection probabilities
  sum_probs = sum(selection_probs)
  selection_probs = [prob/sum_probs for prob in selection_probs]
  
  # Select next city based on selection probabilities
  next_city = random.choices(range(len(cities)), selection_probs)[0]
  return next_city

def update_pheromones(pheromone_matrix, solutions, distances, rho):
  # Calculate pheromone deposition for each edge
  pheromone_deposition = [1 / distance for distance in distances]
  
  # Update pheromone matrix
  for i in range(len(pheromone_matrix)):
    for j in range(len(pheromone_matrix[i])):
      pheromone_matrix[i][j] *= (1 - rho)
      for k in range(len(solutions)):
        if i in solutions[k] and j in solutions[k]:
          pheromone_matrix[i][j] += rho * pheromone_deposition[k]
  return pheromone_matrix

def get_heuristic(city1, city2):
  # Calculate heuristic using Euclidean distance
  x1, y1 = city1
  x2, y2 = city2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calc_distance(cities,solution):
  # Calculate distance of solution path
  distance = 0
  for i in range(len(solution) - 1):
    city1 = cities[solution[i]]
    city2 = cities[solution[i+1]]
    distance += get_heuristic(city1, city2)
  distance += get_heuristic(cities[solution[-1]], cities[solution[0]])
  return distance