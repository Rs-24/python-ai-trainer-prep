# Time to write all of below including tests, explanation and time and aux
# and total space: 25 mins

# Problem: https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l: int, r: int) -> bool:
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True                
        best_left = 0
        best_right = 0
        for left in range(len(s)):
            for right in range(len(s)):
                if left <= right and check(left, right):
                    if right - left >= best_right - best_left:
                        best_left, best_right = left, right
        return s[best_left:best_right+1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("1") == "1"
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("A") == "A"
    assert sol.longestPalindrome("1b2") == "2"
    assert sol.longestPalindrome("A11AB") == "A11A"
    assert sol.longestPalindrome("A11aB") == "11"
    assert sol.longestPalindrome("11") == "11"
    assert sol.longestPalindrome("21") == "1"
    
# Explanation: the code uses a nested loop to check every substring if it's a
# palindrome, then returns the longest found palindrome
# Time: O(n^3), n = len(s)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: worst case O(n)

# Learning lessons (done after completing all of above in 25 mins):
#   - I now realise my solution can be improved to O(n^2) time complexity, my
#     rewrite is below:
#
# def longestPalindrome(self, s: str) -> str:
#     # Time: O(n^2), n = len(s)
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: worst case O(n)
#     if not s:
#         return ""
#     def expand(l: int, r: int):
#         while l >= 0 and r < len(s) and s[l] == s[r]:
#             l -= 1
#             r += 1
#         return l + 1, r - 1
#     best_left = 0
#     best_right = 0
#     for i in range(len(s)):
#         l1, r1 = expand(i, i)
#         l2, r2 = expand(i, i+1)
#         if r1 - l1 >= best_right - best_left:
#             best_left, best_right = l1, r1
#         if r2 - l2 >= best_right - best_left:
#             best_left, best_right = l2, r2
#     return s[best_left: best_right + 1]
#
#   - Additionally, there is another method using dynamic programming using
#     a table of True/False values for all combinations. My attempt is below:
#
# def longestPalindrome(self, s: str) -> str:
#     # Time: O(n^2), n = len(s)
#     # Aux space, excluding output and input: O(n^2)
#     # Total space, including output, excluding input: O(n^2)
#     n = len(s)
#     if n == 0:
#         return ""
#     best_l = best_r = 0
#     store = [[False] * n for _ in range(n)]
#     for length in range(1,n+1):
#         for l in range(n - length + 1):
#             r = l + length - 1
#             if s[l] == s[r]:
#                 if length <= 3 or store[l+1][r-1]:
#                     store[l][r] = True
#                     if length >= best_r - best_l + 1:
#                         best_l, best_r = l, r
#     return s[best_l:best_r+1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestPalindrome("a") == "a"
    assert sol.longestPalindrome("A") == "A"
    assert sol.longestPalindrome("1") == "1"
    assert sol.longestPalindrome("aA") in ("a", "A")
    assert sol.longestPalindrome("a1a") == "a1a"
    assert sol.longestPalindrome("aAb1") in ("a", "A", "b", "1")
    assert sol.longestPalindrome("1111") == "1111"
    assert sol.longestPalindrome("1234") in ("1", "2", "3", "4")


















