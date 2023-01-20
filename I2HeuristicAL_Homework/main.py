# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 21:28:15 2022

@author: ha-ka
"""

import random
import matplotlib.pyplot as plt
import time
from GA import genetic_algorithm
from SA import simulated_annealing
from HC import hill_climbing
from TBS import tabu_search
from ACO import aco
from Permute import permute 
from Distance import get_distance


# Random cities location
cities = [(random.uniform(0,100),random.uniform(0,100)) for _ in range(5)]
# print(permute(points))
Listcities = permute(cities)
init_tourList = []
#----------BRUTE-FORCE SEARCH------------------#
# Start timer
iteration = 0
start_time = time.time()
for i in range(len(Listcities)):
    iteration += 1
    distance = 0
    for j in range(len(Listcities[i])):       
        if j==len(Listcities[i])-1:
            city1 = Listcities[i][0]
            city2 = Listcities[i][j]
        else:
            city1 = Listcities[i][j]
            city2 = Listcities[i][j+1]
        
        # get distance
        distance += get_distance(city1, city2)
        
    # add distance to list
    init_tourList.append(float(distance))
# End timer
end_time = time.time()
# Print Best tour for these City list  ------------v find min distance that is the best tour
print("Using BRUTE-FORCE SEARCH Best tour is: "+str(min(init_tourList)))
# Calculate runtime
run_time = end_time - start_time
print("Using BRUTE-FORCE SEARCH Runtime:", run_time, "seconds")
print("Using BRUTE-FORCE SEARCH Number of iteration: "+str(iteration))
#----------BRUTE-FORCE SEARCH------------------#

citiesPLT = cities + [cities[0]]
# Create Graph 2x3
figure, axis = plt.subplots(2, 3)
# Plot the initial points
axis[0,0].plot([city[0] for city in citiesPLT],[city[1] for city in citiesPLT],'o')


#------------GA----------#
# Start timer
start_time = time.time()
# Optimize the tour
best_tourGA1 = genetic_algorithm(cities,250,0.01,500)
# End timer
end_time = time.time()
# Calculate runtime
run_timeGA = end_time - start_time
print("best tour for GA with pop_size=250 and num_generation = 500 : "+ str(best_tourGA1[0][1]))
best_tourGA = best_tourGA1[0][0]
# print(best_tourGA)
print("RuntimeGA:", run_timeGA, "seconds")


start_time = time.time()
# Optimize the tour
best_tourGA2 = genetic_algorithm(cities,250,0.01,1000)
# End timer
end_time = time.time()
# Calculate runtime
run_timeGA = end_time - start_time
print("best tour for GA  pop_size=250 and num_generation = 1000 : "+ str(best_tourGA2[0][1]))
best_tourGA = best_tourGA2[0][0]
# print(best_tourGA)
print("RuntimeGA:", run_timeGA, "seconds")


start_time = time.time()
# Optimize the tour
best_tourGA3 = genetic_algorithm(cities,500,0.01,500)
# End timer
end_time = time.time()
# Calculate runtime
run_timeGA = end_time - start_time
print("best tour for GA  pop_size=500 and num_generation = 500 : "+ str(best_tourGA3[0][1]))
best_tourGA = best_tourGA3[0][0]
# print(best_tourGA)
print("RuntimeGA:", run_timeGA, "seconds")


start_time = time.time()
# Optimize the tour
best_tourGA4 = genetic_algorithm(cities,500,0.01,1000)
# End timer
end_time = time.time()
# Calculate runtime
run_timeGA = end_time - start_time
print("best tour for GA  pop_size=500 and num_generation = 1000 : "+ str(best_tourGA4[0][1]))
best_tourGA = best_tourGA4[0][0]
# print(best_tourGA)
print("RuntimeGA:", run_timeGA, "seconds")
#------------GA----------#


#------------SA----------#
# Start timer
start_time = time.time()
# Optimize the tour
best_tourSA1 = simulated_annealing(cities, 1000, 0.001, 500)
# End timer
end_time = time.time()
# Calculate runtime
run_timeSA = end_time - start_time
print("best tour for SA num_iterations = 500 : "+ str(best_tourSA1[1]))
best_tourSA = best_tourSA1[0]
print("RuntimeSA:", run_timeSA, "seconds")

# Start timer
start_time = time.time()
# Optimize the tour
best_tourSA2 = simulated_annealing(cities, 1000, 0.001, 1000)
# End timer
end_time = time.time()
# Calculate runtime
run_timeSA = end_time - start_time
print("best tour for SA num_iterations = 1000 : "+ str(best_tourSA2[1]))
best_tourSA = best_tourSA1[0]
print("RuntimeSA:", run_timeSA, "seconds")
#------------SA----------#


#------------HC----------#
# Start timer
start_time = time.time()
# Optimize the tour
best_tourHC = hill_climbing(cities,500)
# End timer
end_time = time.time()
# Calculate runtime
run_timeHC = end_time - start_time
print("best tour for HC num_iterations = 500 : "+ str(best_tourHC[1]))
best_tourHC = best_tourHC[0]
print("RuntimeHC:", run_timeHC, "seconds")

# Start timer
start_time = time.time()
# Optimize the tour
best_tourHC = hill_climbing(cities,1000)
# End timer
end_time = time.time()
# Calculate runtime
run_timeHC = end_time - start_time
print("best tour for HC num_iterations = 1000 : "+ str(best_tourHC[1]))
best_tourHC = best_tourHC[0]
print("RuntimeHC:", run_timeHC, "seconds")
#------------HC----------#


#-----------TBS----------#
# Start timer
start_time = time.time()
# Optimize the tour
best_tourTBS = tabu_search(cities,100,500)
# End timer
end_time = time.time()
# Calculate runtime
run_timeTBS = end_time - start_time
print("best tour for TBS num_iterations = 500 : "+ str(best_tourTBS[1]))
best_tourTBS = best_tourTBS[0]
print("RuntimeTBS:", run_timeTBS, "seconds")

# Start timer
start_time = time.time()
# Optimize the tour
best_tourTBS = tabu_search(cities,100,1000)
# End timer
end_time = time.time()
# Calculate runtime
run_timeTBS = end_time - start_time
print("best tour for TBS num_iterations = 1000 : "+ str(best_tourTBS[1]))
best_tourTBS = best_tourTBS[0]
print("RuntimeTBS:", run_timeTBS, "seconds")
#-----------TBS----------#

# -------------ACO------------#
# Start timer
start_time = time.time()
# Optimize the tour
best_tourACO = aco(cities)
# End timer
end_time = time.time()
# Calculate runtime
run_timeACO = end_time - start_time
print("best tour for ACO num_iterations = 1000 : "+ str(best_tourACO[1]))
best_tourACO = best_tourACO[0]
# print(best_tourACO)
print("RuntimeAOC:", run_timeACO, "seconds")
# -------------ACO------------#
# #print best path and tour




#------------ Plot the optimized tour -----------------------#

#GA
best_tourGA_PLT = best_tourGA + [best_tourGA[0]]
axis[0,1].plot([city[0] for city in best_tourGA_PLT],[city[1] for city in best_tourGA_PLT],'or-')
#SA
best_tourSA_PLT = best_tourSA + [best_tourSA[0]]
axis[0,2].plot([city[0] for city in best_tourSA_PLT],[city[1] for city in best_tourSA_PLT],'or-')
#HC
best_tourHC_PLT = best_tourHC + [best_tourHC[0]]
axis[1,0].plot([city[0] for city in best_tourHC_PLT],[city[1] for city in best_tourHC_PLT],'or-')
#TBS
best_tourTBS_PLT = best_tourTBS + [best_tourTBS[0]]
axis[1,1].plot([city[0] for city in best_tourTBS_PLT],[city[1] for city in best_tourTBS_PLT],'or-')
#ACO
best_tourACO_PLT = best_tourACO + [best_tourACO[0]]
axis[1,2].plot([city[0] for city in best_tourACO_PLT],[city[1] for city in best_tourACO_PLT],'or-')

plt.show()