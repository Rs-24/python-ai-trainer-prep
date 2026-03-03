# Time to write all of below including tests, explanation and time and aux 
# space: 18 mins

# Problem: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x > 9 and x % 10 == 0:
            return False 
        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10

if __name__ == "__main__":
    sol = Solution()
    assert sol.isPalindrome(0) == True
    assert sol.isPalindrome(-1) == False
    assert sol.isPalindrome(1) == True
    assert sol.isPalindrome(5) == True
    assert sol.isPalindrome(11) == True
    assert sol.isPalindrome(121) == True
    assert sol.isPalindrome(1221) == True
    assert sol.isPalindrome(-121) == False
    assert sol.isPalindrome(12231) == False
    assert sol.isPalindrome(120) == False

# Explanation: the code builds each digit of the reversed number while
# removing the rightmost digits of x until x <= rev, then checks if 
# x == rev (if x had an even number of digits) or if x == rev // 10 (if x had
# an odd number of digits)
# Time: O(d), d = number of digits in x
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)


# Full reverse with no strings method:
def isPalindrome(self, x: int) -> bool:
    # Time: O(d), d = number of digits in x
    # Aux space, excluding output and input: O(1)
    # Total space, including output, excluding input: O(1)
    if x < 0:
        return False
    if (x > 9) and (x % 10 == 0):
        return False
    rev = 0
    copy = x
    while copy > 0:
        rev = (rev * 10) + (copy % 10)
        copy //= 10
    return x == rev


# String with two pointers method:
def isPalindrome(self, x: int) -> bool:
    # Time: O(d), d = number of digits in x
    # Aux space, excluding output and input: O(d)
    # Total space, including output, excluding input: O(d)
    if x < 0:
        return False
    if (x > 9) and (x % 10 == 0):
        return False
    s = str(x)
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


