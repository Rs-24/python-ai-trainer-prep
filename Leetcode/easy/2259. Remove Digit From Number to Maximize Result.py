# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        # Time: O(n^2), n = len(number)
        # Space: O(n)
        best = ""
        for i, n in enumerate(number):
            if n == digit:
                best = max(best, number[:i] + number[i + 1:])
        return best


