

class Solution:
    def arrayNesting(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        t = [False] * n
        a = 0
        for i in range(n):
            if not t[i]:
                j = i
                c = 0
                while not t[j]:
                    t[j] = True
                    j = nums[j]
                    c += 1
                a = max(a, c)
        return a


