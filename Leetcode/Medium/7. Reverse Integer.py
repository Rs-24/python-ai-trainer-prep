# Time to write all of below including tests, explanation and time and aux
# and total space: 46 mins

# Problem: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        if negative:
            rev *= -1
        if rev < -(2**31) or rev > (2**31) - 1:
            return 0
        return rev

if __name__ == "__main__":
    sol = Solution()
    assert sol.reverse(-10) == -1
    assert sol.reverse(220) == 22
    assert sol.reverse(-12) == -21
    assert sol.reverse(0) == 0
    assert sol.reverse(123) == 321
    
# Explanation: the code takes abs(x), reverses the digits, adds the negative
# sign back on if x was originally negative and returns it unless it is
# outside the relevant bounds, in which case 0 is returned instead
# Time: O(n), n = x
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)
      
# Learning lessons (done after completing all of above in 46 mins):
#   - I now realise my time complexity comment is wrong, it's actually O(d),
#     where d = number of digits in x
#   - Additionally, there is another method which prevents overflow. My
#     attempt is below:
#
# def reverse(self, x: int) -> int:
#     # Time: O(d), d = number of digits in x
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(1)
#     negative = x < 0
#     x = abs(x)
#     rev = 0
#     limit = 2**31 if negative else (2**31) - 1
#     while x > 0:
#         digit = x % 10
#         if rev > limit // 10 or (rev == limit // 10 and digit > limit % 10):
#             return 0
#         rev = rev * 10 + digit
#         x //= 10
#     if negative:
#         rev *= -1
#     return rev












