# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/description/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        # Time: O(m + n + k), m = len(firstWord), n = len(secondWord), k = len(targetWord)
        # Space: O(1)
        def convert(s: str) -> int:
            num = 0
            for ch in s:
                num = num * 10 + ord(ch) - ord("a")
            return num
        return convert(firstWord) + convert(secondWord) == convert(targetWord)


