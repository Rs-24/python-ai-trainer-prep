

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> list:
        # Time: O(log_x bound + log_y bound)
        # Space: O(n)
        s = set()
        a = 1
        while a <= bound:
            b = 1
            while a + b <= bound:
                s.add(a + b)
                if y == 1:
                    break
                b *= y
            if x == 1:
                break
            a *= x
        return list(s)


        