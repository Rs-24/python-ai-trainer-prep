

class Solution:
    def countAsterisks(self, s: str) -> int:
        # Time: O(n)
        # Space: O(1)
        count = 0
        in_pair = False
        for ch in s:
            if ch == "|":
                in_pair = not in_pair
            count += 1 if ch == "*" and not in_pair else 0
        return count


