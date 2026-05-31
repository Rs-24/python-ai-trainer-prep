

class Solution:
    def minimumSum(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        n = len(nums)
        l = [float("inf")]
        m = nums[0]
        for i in range(1, len(nums)):
            l.append(m)
            m = min(m, nums[i])
        r = [float("inf")]
        m = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            r.append(m)
            m = min(m, nums[i])
        r.reverse()
        b = float("inf")
        for i, num in enumerate(nums):
            if l[i] < num and r[i] < num:
                b = min(b, l[i] + num + r[i])
        return b if b != float("inf") else -1


