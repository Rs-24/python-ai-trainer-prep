# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-key-of-the-numbers/description/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Time: O(1)
        # Space: O(1)
        num1 = "0" * (4 - len(str(num1))) + str(num1)
        num2 = "0" * (4 - len(str(num2))) + str(num2)
        num3 = "0" * (4 - len(str(num3))) + str(num3)
        key = []
        for i in range(4):
            key.append(min(num1[i], num2[i], num3[i]))
        return int("".join(key))


