# Time to write all of below including tests, explanation and time and aux
# and total space: 11 mins

# Problem: https://leetcode.com/problems/perfect-number/description/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Time: O(n), n = num
        # Space: O(1)
        divisor = 1
        total = 0
        while divisor <= num // 2:
            if num % divisor == 0:
                total += divisor
            divisor += 1
        return total == num

# O(sqrt(n)) time method:
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Time: O(sqrt(n)), n = num
        # Space: O(1)
        if num == 1:
            return False
        i = 1
        total = 0
        while i ** 2 <= num:
            if num % i == 0:
                total += i
                if num // i != i and num // i != num:
                    total += (num // i)
            i += 1
        return total == num


