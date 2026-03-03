# Time to write all of below including tests, explanation and time and aux 
# space: 12 mins

# Problem: https://leetcode.com/problems/two-sum/description/

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i

if __name__ == "__main__":
    sol = Solution()
    assert sorted(sol.twoSum([1, 2], 3)) == sorted([0, 1])
    assert sorted(sol.twoSum([-1, 0, 1], 0)) == sorted([0, 2])
    assert sorted(sol.twoSum([-1, 0, 1], -1)) == sorted([0, 1])
    assert sorted(sol.twoSum([1, 2, 3, 4], 7)) == sorted([2, 3])

# Explanation: the code stores numbers and their corresponding indices in the
# dictionary seen. The program iterates through nums and calculates diff,
# and if diff is in seen, then a list containing the relevant indices is
# returned
# Time: O(n), n = len(nums)
# Space: excluding output: O(n)

