

class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        out = []
        cur = 0
        for num in nums:
            cur <<= 1
            cur |= num
            out.append(cur % 5 == 0)
        return out


