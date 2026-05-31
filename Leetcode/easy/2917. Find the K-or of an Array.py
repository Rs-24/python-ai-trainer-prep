

class Solution:
    def findKOr(self, nums: list, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        ans = 0
        for b in range(32):
            c = 0
            for num in nums:
                c += (num >> b) & 1
            ans |= (c >= k) << b
        return ans


