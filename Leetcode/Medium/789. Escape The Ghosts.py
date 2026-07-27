

class Solution:
    def escapeGhosts(self, ghosts: list, target: list) -> bool:
        # Time: O(n)
        # Space: O(1)
        return all(abs(x - target[0]) + abs(y - target[1]) > abs(target[0]) + abs(target[1]) for x, y in ghosts)


