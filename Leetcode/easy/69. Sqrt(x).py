

class Solution:
    def mySqrt(self, x: int) -> int:
        # Time: O(log x)
        # Space: O(1)
        if x < 2:
            return x
        l, r = 0, x // 2
        while l <= r:
            mid = (l + r) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                l = mid + 1
            else:
                r = mid - 1
        return r


