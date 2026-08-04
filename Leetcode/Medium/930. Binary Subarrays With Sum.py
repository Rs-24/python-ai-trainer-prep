

class Solution:
    def numSubarraysWithSum(self, nums: list, goal: int) -> int:
        # Time: O(n)
        # Space: O(n)
        d = {0: 1}
        t = a = 0
        for x in nums:
            t += x
            a += d.get(t - goal, 0)
            d[t] = d.get(t, 0) + 1
        return a


        