# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/maximum-containers-on-a-ship/description/

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        # Time: O(1)
        # Space: O(1)
        return min(n * n, maxWeight // w)


