# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/check-balanced-string/description/

class Solution:
    def isBalanced(self, num: str) -> bool:
        # Time: O(n), n = len(num)
        # Space: O(1)
        even = 0
        odd = 0
        for i, d in enumerate(num):
            if i % 2 == 0:
                even += int(d)
            else:
                odd += int(d)
        return even == odd


