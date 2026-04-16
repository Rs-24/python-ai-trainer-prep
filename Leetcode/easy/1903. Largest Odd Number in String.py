# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/largest-odd-number-in-string/description/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Time: O(n), n = len(num)
        # Space, excluding output: O(1)
        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) % 2 != 0:
                return num[:i + 1]
        return ""


