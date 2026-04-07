# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/determine-if-string-halves-are-alike/description/

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Time: O(n), n = len(s)
        # Space: O(1)
        n = len(s)
        total1 = 0
        total2 = 0
        for i, ch in enumerate(s):
            if ch.lower() in "aeiou":
                if i < n // 2:
                    total1 += 1
                else:
                    total2 += 1
        return total1 == total2


