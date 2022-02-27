import math
import os
import random
import re
import sys

#
# Complete the 'whatFlavors' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. INTEGER money
#

def whatFlavors(cost, money):
    # Write your code here
    
    flavors = {}
    
    i = 0
    for i in range(len(cost)):
        if money - cost[i] in flavors:
            chosen_flavor = [flavors[money - cost[i]] + 1, i + 1]
        else:
            flavors[cost[i]] = i
        i += 1
        
    print(f"{chosen_flavor[0]} {chosen_flavor[1]}")
    
whatFlavors([1, 2, 3, 5, 6], 5) # 2 3
