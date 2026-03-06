# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Time: O(1)
        # Space: O(1)
        return n > 0 and (n & (n - 1)) == 0

# Loop by dividing by 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Time: O(log_2 n)
        # Space: O(1)
        if n <= 0:
            return False       
        while n % 2 == 0:
            n //= 2
        return n == 1


