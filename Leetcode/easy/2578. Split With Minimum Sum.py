# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/split-with-minimum-sum/description/

class Solution:
    def splitNum(self, num: int) -> int:
        # Time: O(d log d), d = number of digits in num
        # Space: O(d)
        s = sorted(str(num))
        num1, num2 = [], []
        for i, ch in enumerate(s):
            if i % 2 == 0:
                num1.append(ch)
            else:
                num2.append(ch)
        return int("".join(num1)) + int("".join(num2))


