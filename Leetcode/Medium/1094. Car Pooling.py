

class Solution:
    def carPooling(self, trips: list, capacity: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        d = [0] * 1001
        for p, s, e in trips:
            d[s] += p
            d[e] -= p
        t = 0
        for x in d:
            t += x
            if t > capacity:
                return False
        return True


