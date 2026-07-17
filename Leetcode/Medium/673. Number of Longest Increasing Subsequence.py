

class Solution:
    def findNumberOfLIS(self, nums: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        n = len(nums)
        l = [1] * n
        f = [1] * n
        m = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if l[j] + 1 > l[i]:
                        l[i] = l[j] + 1
                        f[i] = f[j]
                    elif l[j] + 1 == l[i]:
                        f[i] += f[j]
            m = max(m, l[i])
        a = 0
        for i in range(n):
            if l[i] == m:
                a += f[i]
        return a


