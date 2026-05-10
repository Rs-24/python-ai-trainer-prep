

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # Time: O(n), n = len(bills)
        # Space: O(1)
        f = t = 0
        for b in bills:
            if b == 5:
                f += 1
            elif b == 10:
                if f == 0:
                    return False
                t += 1
                f -= 1
            else:
                if f >= 1 and t >= 1:
                    f -= 1
                    t -= 1
                elif f >= 3:
                    f -= 3
                else:
                    return False
        return True


