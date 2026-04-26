# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # Time: O(1)
        # Space: O(1)
        cycle = 2 * (n - 1)
        place = time % cycle
        return place + 1 if place < n else n - (place - (n - 1))


