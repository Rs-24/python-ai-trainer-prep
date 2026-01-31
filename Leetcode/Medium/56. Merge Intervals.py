# 8 + 13 - 

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        out = []

        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i <= j: 
                    continue

                element = [None, None]

                a1, b1 = intervals[i][0], intervals[i][1]                
                a2, b2 = intervals[j][0], intervals[j][1]

                if a1 >= a2 and b1 <= b2:
                    element = [a2, b2]
                elif a2 >= a1 and b2 <= b1:
                    element = [a1, b1]
                elif 
                    




