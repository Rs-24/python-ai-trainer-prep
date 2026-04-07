# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        # Time: O(log n), n = num
        # Space: O(1)
        total = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            total += 1
        return total


