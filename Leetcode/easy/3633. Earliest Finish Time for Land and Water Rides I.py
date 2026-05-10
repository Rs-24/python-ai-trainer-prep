# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/description/

from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # Time: O(m + n), m = len(landStartTime) = len(landDuration), n = len(waterstartTime) = len(waterDuration)
        # Space: O(1)
        def calc(start1, dur1, start2, dur2) -> int:
            switch = min(s + d for s, d in zip(start1, dur1))
            end = switch
            for s, d in zip(start2, dur2):
                end = min(end, max(switch, s) + d)
            return end       
        return min(calc(landStartTime, landDuration, waterStartTime, waterDuration), calc(waterStartTime, waterDuration, landStartTime, landDuration))


