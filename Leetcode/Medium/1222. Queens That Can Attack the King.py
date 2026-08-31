

class Solution:
    def queensAttacktheKing(self, queens: list, king: list) -> list:
        # Time: O(1)
        # Space: O(1)
        queens = set(map(tuple, queens))
        ans = []
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, -1), (-1, 1), (1, 1), (-1, -1)]:
            x, y = king[0] + dx, king[1] + dy
            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queens:
                    ans.append([x, y])
                    break
                x += dx
                y += dy
        return ans


