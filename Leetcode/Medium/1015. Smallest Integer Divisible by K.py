

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # Time: O(k)
        # Space: O(1)
        if k % 2 == 0 or k % 5 == 0:
            return -1
        r = 0
        for l in range(1, k + 1):
            r = (r * 10 + 1) % k
            if r == 0:
                return l
        return -1


