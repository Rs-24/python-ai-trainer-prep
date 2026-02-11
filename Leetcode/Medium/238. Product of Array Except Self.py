# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 24 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/product-of-array-except-self/description/

from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = [1] * n
        for i in range(1, n):
            out[i] = nums[i - 1] * out[i - 1]
        multiplier = 1
        for i in range(n - 2, -1, -1):
            multiplier *= nums[i + 1]
            out[i] *= multiplier
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1, 2]) == [2, 1]
    assert sol.productExceptSelf([-1, 0, 1]) == [0, -1, 0]
    assert sol.productExceptSelf([1, 1, 2, 3, 4]) == [24, 24, 12, 8, 6]

# Explanation: the code first finds the product of all numbers in nums to the
# left of i, and then multiplies this by the product of all numbers in nums 
# to the right of i
# Time: O(n), n = len(nums)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 1h 24 mins):
#   - No major learning lessons












