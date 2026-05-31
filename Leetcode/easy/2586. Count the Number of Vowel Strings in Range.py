

class Solution:
    def vowelStrings(self, words: list, left: int, right: int) -> int:
        # Time: O(n)
        # Space: O(1)
        return sum(1 for i in range(left, right + 1) if words[i][0] in "aeiou" and words[i][-1] in "aeiou")


