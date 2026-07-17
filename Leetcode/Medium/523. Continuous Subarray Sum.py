

class Solution:
    def checkSubarraySum(self, nums: list, k: int) -> bool:
        # Time: O(n)
        # Space: O(n)
        s = 0
        d = {0: -1}
        for i, x in enumerate(nums):
            s += x
            t = s % k
            if t in d:
                if i - d[t] > 1:
                    return True
            else:
                d[t] = i
        return False


