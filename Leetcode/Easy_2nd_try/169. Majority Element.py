# Time to write all of below including tests, explanation and time and aux 
# space: 11 mins

# Problem: https://leetcode.com/problems/majority-element/description/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
            if count == 0:
                candidate = num
                count = 1
        return candidate

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([1]) == 1
    assert sol.majorityElement([-1, 0, 0]) == 0
    assert sol.majorityElement([1, 2, 2, 2, 3]) == 2
    assert sol.majorityElement([1, 1, 1, 2, 3]) == 1
    assert sol.majorityElement([1, 2, 3, 3, 3]) == 3

# Explanation: the code takes the first number as the candidate, and stores
# its count, and iterates through the rest of the list. If the current
# number is equal to candidate, then count is incremented, and if not, then
# it is decremented. If count == 0, then candidate is set to the current
# number, and count is set to 1. Once the loop ends, candidate is returned
# Time: O(n), n = len(nums)
# Space: O(1)

# Learning lessons (done after completing all of above in 11 mins):
#   - Additionally, there is an even simpler method which uses the .sort()
#     function. My attempt is below:
#
# def majorityElement(self, nums: List[int]) -> int:
#     # Time: O(n log n), n = len(nums)
#     # Space: worst case O(n)
#     nums.sort()
#     return nums[len(nums) // 2]























































































