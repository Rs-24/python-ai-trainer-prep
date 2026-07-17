

class Solution:
    def findLength(self, nums1: list, nums2: list) -> int:
        # Time: O(m * n)
        # Space: O(n)
        m, n = len(nums1), len(nums2)
        dp = [0] * (n + 1)
        a = 0
        for i in range(m - 1, -1, -1):
            t = [0] * (n + 1)
            for j in range(n - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    t[j] = 1 + dp[j + 1]
                    a = max(a, t[j])
            dp = t
        return a


