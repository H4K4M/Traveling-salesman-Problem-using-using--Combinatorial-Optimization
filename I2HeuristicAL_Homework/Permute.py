# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 13:37:01 2022

@author: ha-ka
"""

def permute(nums):
    
    def backtrack(first=0):
        # iteration = iteration + 1
        # if all integers are used up
        if first == n:
            output.append(nums[:])
        for i in range(first, n):
            # place i-th integer first
            # in the current permutation
            nums[first], nums[i] = nums[i], nums[first]
            # use next integers to complete the permutations
            backtrack(first + 1)
            # backtrack
            nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    iteration = 0
    backtrack()
    return output

