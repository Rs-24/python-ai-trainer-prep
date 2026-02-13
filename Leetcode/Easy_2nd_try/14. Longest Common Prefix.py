# Time to write all of below including tests, why the solution works and time 
# and space complexity: 36 minutes

# Problem: https://leetcode.com/problems/longest-common-prefix/description/ 

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strings = []
        temp = []
        for s in strs:
            if s == "":
                return ""
            temp = []
            for ch in s:
                temp.append(ch)
            strings.append(temp)
        min_length = len(min(strings))
        prefix = [strings[0][0]]
        while len(prefix) <= min_length:
            length = len(prefix)
            for s in strings:
                if s[0:length] != prefix:
                    if length == 1:
                        return ""
                    return "".join(prefix[0:length - 1])
            if length == min_length:
                return "".join(prefix[0:length])
            prefix.append(strings[0][length])
            
if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["hi"]) == "hi"
    assert sol.longestCommonPrefix([""]) == ""
    assert sol.longestCommonPrefix(["", ""]) == ""
    assert sol.longestCommonPrefix(["hi", "hello", "hiya"]) == "h"
    assert sol.longestCommonPrefix(["", "hello", "hiya"]) == ""
    assert sol.longestCommonPrefix(["hi", "Bye", "Goodbye"]) == ""
    assert sol.longestCommonPrefix(["hi", "hi", "hi"]) == "hi"
    assert sol.longestCommonPrefix(["hi", "hiya", "hidden"]) == "hi"

# Explanation: the code converts each string to a list, and stores each list 
# in a new list called strings. Then it builds a prefix using the first
# element in strings, and compares this prefix to the corresponding prefix in
# every other element in strings
# Time: O(c + L * n), c = total number of characters in strs, L = length of
# shortest string in strs, n = number of strings in strs
# Aux space, excluding output and input: O(c)
# Total space, including output, excluding input: O(c)

# Learning lessons (done after completing all of above in 36 minutes):
#   - I now realise my solution can be simplified, my rewrite is below:
#
# def longestCommonPrefix(self, strs: List[str]) -> str:
#     # Time: O(n * m), n = length of shortest string in strs, m = number of 
#     # strings in strs
#     # Aux space, excluding output and input: O(1)
#     # Total space, including output, excluding input: O(n)
#     right = 0
#     for ch in strs[0]:
#         if not all(len(s) >= (right + 1) and ch == s[right] for s in strs):
#             return strs[0][:right]
#         right += 1
#     return strs[0]







