

class Solution:
    def robotSim(self, commands: list, obstacles: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set(map(tuple, obstacles))
        t = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = a = d = 0
        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = t[d]
                for _ in range(c):
                    if (x + dx, y + dy) in s:
                        break
                    x += dx
                    y += dy
                    a = max(a, x * x + y * y)
        return a


        