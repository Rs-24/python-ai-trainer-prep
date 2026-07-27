

class Solution:
    def maxDistToClosest(self, seats: list) -> int:
        # Time: O(n)
        # Space: O(1)
        a, p = 0, -1
        for i, s in enumerate(seats):
            if s == 1:
                if p == -1:
                    a = i
                else:
                    a = max(a, (i - p) // 2)
                p = i
        a = max(a, len(seats) - 1 - p)
        return a


        