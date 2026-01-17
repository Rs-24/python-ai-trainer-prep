# Time to write all of below including tests, explanation and time and aux 
# space: 8 mins

# Problem: https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i != j and n1 + n2 == target:
                    return [i, j]

# Tests:
# [1, 2], 3 -> [0, 1]
# [-1, 0, 1], 0 -> [0, 2]
# [1, 2, -3], -1 -> [1, 2] 

# Explanation: nums is iterated over in two separate loops until a sum is
# found, and when so the corresponding indices are returned
# Time: O(n^2), n = len(nums)
# Aux space: O(1)

# Learning lessons (done after completing all of above in 8 mins):
#   - Ideally it would be better to find an O(n) solution. My rewrite is below:
#
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     # Time: O(n), n = len(nums)
#     # Aux space: O(n)
#     seen = {}
#     for i, n in enumerate(nums):
#         diff = target - n
#         if diff in seen:
#             return [seen[diff], i]
#         seen[n] = i
#
#   - Also, I could have used asserts for my tests and added a duplicate
#     test. My rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.twoSum([1, 2], 3) == [0, 1]
#     assert sol.twoSum([-1, 0, 1], 0) == [0, 2]
#     assert sol.twoSum([1, 2, -3], -1) == [1, 2]
#     assert sol.twoSum([3, 3], 6) == [0, 1]
    








