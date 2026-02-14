# Time to write all of below including tests, why the solution works and time 
# and space complexity: 25 mins

# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        elif len(needle) == len(haystack):
            return 0 if needle == haystack else -1
        
        i = j = 0
        while i < len(haystack) and j < len(needle):
            if haystack[i] == needle[j]:
                j += 1
            else:
                j = 0
            i += 1
        
        if j == len(needle):
            return i - j
        else:
            return -1

if __name__ == "__main__":
    sol = Solution()
    assert sol.strStr("b", "a") == -1
    assert sol.strStr("a", "a") == 0
    assert sol.strStr("b", "ab") == -1
    assert sol.strStr("bb", "a") == -1
    assert sol.strStr("abab", "a") == 0
    assert sol.strStr("byehibye","hi") == 3
    assert sol.strStr("worship", "ship") == 3
    assert sol.strStr("worshi", "ship") == -1

# Explanation: the code iterates through both needle and haystack using the
# pointers i and j. The haystack pointer (i) is incremented regardless, and
# the needle pointer (j) is only incremented if haystack[i] == needle[j].
# At the end, the code checks whether j == len(needle), and if so i - j is 
# returned, otherwise -1 is returned
# Time: worst case O(n), n = len(haystack) if len(haystack) > len(needle)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 25 mins):
#   - I now realise my solution can be improved, my rewrite is below:
#
# def strStr(self, haystack: str, needle: str) -> int:
#     # Time: O((h - n + 1) * n), h = len(haystack), n = len(needle)
#     # Aux space, excluding output and input: O(n)
#     # Total space, including output, excluding input: O(n)    
#     h = len(haystack)
#     n = len(needle)
#     if h < n:
#         return -1
#     elif h == n:
#         return 0 if haystack == needle else -1
#     for i in range(h - n + 1):
#         if haystack[i:i+n] == needle:
#             return i
#     return -1





