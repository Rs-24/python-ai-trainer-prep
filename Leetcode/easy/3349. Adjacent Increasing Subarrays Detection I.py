

class Solution:
    def hasIncreasingSubarrays(self, nums: list, k: int) -> bool:
        # Time: O(n)
        # Space: O(1)
        p, c = 0, 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                c += 1
            else:
                p = c
                c = 1
            if (p >= k and c >= k) or p >= 2 * k or c >= 2 * k:
                return True
        return False


