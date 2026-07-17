

class Solution:
    def constructArray(self, n: int, k: int) -> list:
        # Time: O(n)
        # Space: O(n)
        a = []
        l, r = 1, k + 1
        while l <= r:
            a.append(l)
            l += 1
            if l <= r:
                a.append(r)
                r -= 1
        a.extend(range(k + 2, n + 1))
        return a


