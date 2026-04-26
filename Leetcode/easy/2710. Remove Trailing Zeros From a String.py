# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/remove-trailing-zeros-from-a-string/description/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # Time: O(n), n = len(num)
        # Aux space: O(1)
        i = len(num) - 1
        while i >= 0:
            if num[i] != "0":
                break
            i -= 1
        return num[:i + 1]


