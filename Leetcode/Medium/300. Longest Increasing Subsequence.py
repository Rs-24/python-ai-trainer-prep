# Time to write all of below including tests, explanation and time and aux
# and total space: 36 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/longest-increasing-subsequence/description/

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    assert sol.lengthOfLIS([]) == 0
    assert sol.lengthOfLIS([1]) == 1
    assert sol.lengthOfLIS([1, 2, 3]) == 3
    assert sol.lengthOfLIS([3, 2, 1]) == 1
    assert sol.lengthOfLIS([-1, 0, 1, 2, -4, 5, 4, 6]) == 6

# Explanation: the code stores the length of the longest strictly increasing
# subsequence up to index i in the list dp, and iterates through nums while
# trying to find if the value at the current index is larger than any previous
# value and if so, assigns the same index in dp to max(dp[i], dp[j] + 1) where
# i is the current index and j is the index of the element in nums which nums[i]
# is greater than
# Time: O(n^2), n = len(nums)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 36 mins):
#   - I now realise there is another version with O(n log n) time complexity,
#     my attempt is below:
#
# from bisect import bisect_left
# def lengthOfLIS(self, nums: List[int]) -> int:
#     # Time: O(n log n), n = len(nums)
#     # Aux space, excluding output and input: O(L), L = maximum length reached
#     # by tails, worst case O(n)
#     # Total space, including output, excluding input: O(L), worst case O(n)
#     tails = []
#     for num in nums:
#         i = bisect_left(tails, num)
#         if i == len(tails):
#             tails.append(num)
#         else:
#             tails[i] = num    
#     return len(tails)
#
#   - I also realise my tests could have been improved, my rewrite is below:
#
# if __name__ == "__main__":
#     sol = Solution()
#     assert sol.lengthOfLIS([]) == 0
#     assert sol.lengthOfLIS([1]) == 1
#     assert sol.lengthOfLIS([1, 2, 3]) == 3
#     assert sol.lengthOfLIS([3, 2, 1]) == 1
#     assert sol.lengthOfLIS([-1, 0, 1, 2, -4, 5, 4, 6]) == 6
#     assert sol.lengthOfLIS([2, 2, 2]) == 1
    











