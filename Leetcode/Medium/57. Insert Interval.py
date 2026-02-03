# 69

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        out = []

        for a, b in intervals:
            if newInterval[0] <= b:
                b = max(b, )





        intervals.append(newInterval)
        combined = sorted(intervals, key=lambda x: x[0])
        out = []
        interval_start = combined[0][0]
        prev_end = combined[0][1]
        for interval in combined[1:]:
            if interval[0] <= prev_end:
                prev_end = max(prev_end, interval[1])
            else:
                out.append([interval_start, prev_end])
                interval_start = interval[0]
                prev_end = interval[1]
        out.append([interval_start, prev_end])
        return out





