# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 21:51:46 2022

@author: ha-ka
"""
import math

def calc_distance(individual):
  # Calculate distance of individual's path
  distance = 0
  for i in range(len(individual) - 1):
    distance += get_distance(individual[i], individual[i+1])
    
  distance += get_distance(individual[-1], individual[0])
  return distance

def get_distance(city1, city2):
  # Calculate distance between two cities using Euclidean distance
  x1, y1 = city1
  x2, y2 = city2
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)