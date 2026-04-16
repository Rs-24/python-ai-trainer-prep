# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Time: O(n), n = len(num)
        # Space: O(1)
        best = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                best = max(best, num[i:i + 3])
        return best


