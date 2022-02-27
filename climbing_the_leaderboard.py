import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    ranked = sorted(list(set(ranked)))
    
    res = []
    i = 0
    length = len(ranked)
    for score in player:
        while i < length and score >= ranked[i]:
            i += 1
        res.append(length - i + 1)
        
    return res
    
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120])) # [6, 4, 2, 1]
