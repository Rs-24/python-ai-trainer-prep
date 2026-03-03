# Time to write all of below including tests, explanation and time and aux
# and total space: 26 mins

# Problem: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        negative = x < 0
        limit = 2**31 if negative else 2**31 - 1
        x = abs(x)
        while x > 0:
            if rev > ((limit - (x % 10)) // 10):
                return 0
            rev = rev * 10 + (x % 10)
            x //= 10
        return rev * (-1) if negative else rev

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverse(-10) == -1
    assert sol.reverse(220) == 22
    assert sol.reverse(-12) == -21
    assert sol.reverse(0) == 0
    assert sol.reverse(123) == 321
    
# Explanation: the code takes abs(x) and reverses the digits while checking
# if it is within the required range, then adds the negative sign back on if x
# was originally negative
# Time: O(d), d = number of digits in x
# Space: O(1)
    

