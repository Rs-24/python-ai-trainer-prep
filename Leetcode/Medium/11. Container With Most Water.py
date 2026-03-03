# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/container-with-most-water/description/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        current = 0
        while l < r:
            current = (r - l) * min(height[l], height[r])
            best = max(best, current)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return best

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1, 2]) == 1
    assert sol.maxArea([0, 2]) == 0
    assert sol.maxArea([1, 2, 3]) == 2
    assert sol.maxArea([3, 2, 4]) == 6
    
# Explanation: The program uses two pointers at either end, and gradually
# brings both pointers to the middle while checking if the current area is
# greater than best. When decrementing, it decrements the pointer with the
# lower height
# Time: O(n), n = len(height)
# Space: O(1)


