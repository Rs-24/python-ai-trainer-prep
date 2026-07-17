

class Solution:
    def validSquare(self, p1: list, p2: list, p3: list, p4: list) -> bool:
        # Time: O(1)
        # Space: O(1)
        a = [p1, p2, p3, p4]
        t = []
        for i in range(4):
            for j in range(i + 1, 4):
                t.append((a[i][0] - a[j][0]) ** 2 + (a[i][1] - a[j][1]) ** 2)
        t.sort()
        return t[0] > 0 and t[0] == t[1] == t[2] == t[3] and t[4] == t[5] and t[4] == 2 * t[0]


