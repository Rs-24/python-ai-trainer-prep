

class Solution:
    def findMaxLength(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        d = {0: -1}
        t = a = 0
        for i, x in enumerate(nums):
            if x == 0:
                t -= 1
            else:
                t += 1
            if t in d:
                a = max(a, i - d[t])
            else:
                d[t] = i
        return a


