# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-residue-prefixes/description/

class Solution:
    def residuePrefixes(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        seen = set()
        count = 0
        for i, ch in enumerate(s):
            seen.add(ch)
            if len(seen) == (i + 1) % 3:
                count += 1
        return count


