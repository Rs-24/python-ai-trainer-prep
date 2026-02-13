# Time to write all of below including tests, explanation and time and aux 
# space: 16 mins

# Problem: https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        out = []
        for i, num in enumerate(nums):
            required = target - num
            if required in seen:
                for j in range(len(nums)):
                    if i != j and nums[j] == required:
                        out.append(j)
                out.append(i)
                return out
            seen.add(num)
    
if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.twoSum([1, 2], 3)) == sorted([0, 1])
    assert sorted(sol.twoSum([1, 1], 2)) == sorted([0, 1])
    assert sorted(sol.twoSum([0, 0], 0)) == sorted([0, 1])
    assert sorted(sol.twoSum([-1, 2, 3], 2)) == sorted([0, 2])
    assert sorted(sol.twoSum([1, 2, 3, -3], 0)) == sorted([2, 3])
    assert sorted(sol.twoSum([1, 2, 3, -3], -2)) == sorted([0, 3])
    
# Explanation: the code iterates through the list using a set to store seen
# values, and if the required value is in seen, finds the index of the
# required value and outputs this index along with the current index in the
# form of a list
# Time: O(n), n = len(nums)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 16 mins):
#   - I now realise my solution can be improved, my rewrite is below:
#
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#     # Time: O(n), n = len(nums)
#     # Aux space, excluding output and input: worst case O(n)
#     # Total space, including output, excluding input: worst case O(n)
#     seen = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], i]
#         seen[num] = i


