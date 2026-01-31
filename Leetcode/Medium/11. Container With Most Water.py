# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if i == j:
                    continue
                area = abs(j - i) * min(height[j], height[i])
                best = max(best, area)
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 2]) == 1
    assert sol.maxArea([0, 2]) == 0
    assert sol.maxArea([1, 2, 3]) == 2
    assert sol.maxArea([3, 2, 4]) == 6
    
# Explanation: The program finds the area for every combination of two lines
# and outputs the largest area found      
# Time: O(n^2), n = len(height)
# Aux space, excluding output and input: O(1)
# Total space, including output and input: O(1)

# Learning lessons (done after completing all of above in 11 mins):
#   - I now realise there is an O(n) time solution, my attempt is below:
#
# def maxArea(self, height: List[int]) -> int:
#     # Time: O(n), n = len(height)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     l, r = 0, len(height) - 1
#     best = 0
#     while l < r:
#         area = (r - l) * min(height[l], height[r])
#         best = max(best,area)
#         if height[l] < height[r]:
#             l += 1
#         else:
#             r -= 1
#     return best



