

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        # Time: O(n log n)
        # Space: O(n)
        t = []
        for x in nums:
            i = bisect_left(t, x)
            if i == len(t):
                t.append(x)
            else:
                t[i] = x
        return len(t)
 

