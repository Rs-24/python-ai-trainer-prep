

class Solution:
    def longestConsecutive(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(nums)
        b = 0
        for x in s:
            if x - 1 not in s:
                t = 1
                c = x
                while c + 1 in s:
                    c += 1
                    t += 1
                b = max(b, t)
        return b


