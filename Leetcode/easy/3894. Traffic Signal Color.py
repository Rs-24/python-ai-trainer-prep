# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/traffic-signal-color/description/

class Solution:
    def trafficSignal(self, timer: int) -> str:
        # Time: O(1)
        # Space: O(1)
        if timer == 0:
            return "Green"
        if timer == 30:
            return "Orange"
        if 30 < timer <= 90:
            return "Red"
        return "Invalid" 


