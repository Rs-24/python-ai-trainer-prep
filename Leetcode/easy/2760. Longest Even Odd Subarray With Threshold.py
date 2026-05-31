

class Solution:
    def longestAlternatingSubarray(self, nums: list, threshold: int) -> int:
        # Time: O(n)
        # Space: O(1)
        n = len(nums)
        best = 0
        i = 0
        while i < n:
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < n and nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                    j += 1
                best = max(best, j - i)
                i = j
            else:
                i += 1
        return best


