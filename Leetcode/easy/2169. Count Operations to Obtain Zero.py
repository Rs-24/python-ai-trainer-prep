# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-operations-to-obtain-zero/description/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # Time: O(n), n = max(num1, num2)
        # Space: O(1)
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count


