# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/maximum-69-number/description/

class Solution:
    def maximum69Number(self, num: int) -> int:
        # Time: O(n), n = log(num)
        # Space: O(n)
        converted = False
        ans = 0
        for ch in str(num):
            if ch == "6" and not converted:
                ans = ans * 10 + 9
                converted = True
            else:
                ans = ans * 10 + int(ch)
        return ans


