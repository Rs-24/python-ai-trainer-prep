# Time to write all of below including tests, explanation and time and aux 
# space: 10 mins

# Problem: https://leetcode.com/problems/majority-element/description/

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqs = {}
        for i, num in enumerate(nums):
            freqs[num] = freqs.get(num, 0) + 1
        most = max(freqs.values())

        for num in freqs:
            if freqs[num] == most:
                return num

if __name__ == "__main__":
    sol = Solution()
    assert sol.majorityElement([1]) == 1
    assert sol.majorityElement([-1, 0, 1, 1]) == 1
    assert sol.majorityElement([1, 1, 2, 2, 2, 3, 3]) == 2
    assert sol.majorityElement([3, 3, 3]) == 3

# Explanation: The function iterates through the list, and stores a dictionary
# of each number and its frequency. The number with the highest frequency is
# outputted
# Time: O(n), n = len(nums)
# Aux space, excluding output and input: O(n)  
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 10 mins):
#   - There is also an O(1) space version. My attempt is below:
#
# def majorityElement(self, nums: List[int]) -> int:
#     # Time: O(n), n = len(nums)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     count = 0
#     candidate = None
#     for num in nums:
#         if count == 0:
#             candidate = num
#         count += 1 if num == candidate else -1
#     return candidate
#
#   - Additionally, there is an even simpler method which uses the .sort()
#     function. My attempt is below:
#
# def majorityElement(self, nums: List[int]) -> int:
#     # Time: O(n log n)
#     # Aux space, excluding output and input: O(1) - O(n) depending on sorting implementation, as Python's sort may use extra memory
#     # Total space, including output, excluding input: O(1) - O(n) depending on sorting implementation, as Python's sort may use extra memory
#     nums.sort()
#     return nums[len(nums)//2]








