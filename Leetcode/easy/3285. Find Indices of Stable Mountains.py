# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-indices-of-stable-mountains/description/

from typing import List

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        # Time: O(n), n = len(height)
        # Space: O(n)
        out = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                out.append(i)
        return out


