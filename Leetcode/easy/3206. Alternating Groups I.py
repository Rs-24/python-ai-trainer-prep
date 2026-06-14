

class Solution:
    def numberOfAlternatingGroups(self, colors: list) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for i in range(len(colors)) if colors[i] != colors[(i + 1) % len(colors)] and colors[i] != colors[(i - 1) % len(colors)])


