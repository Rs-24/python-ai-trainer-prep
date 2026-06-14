

class Solution:
    def evenNumberBitwiseORs(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(1)
        ans = 0
        for n in nums:
            ans |= n if n % 2 == 0 else 0
        return ans


