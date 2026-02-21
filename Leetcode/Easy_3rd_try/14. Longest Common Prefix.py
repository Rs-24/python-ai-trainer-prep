# Time to write all of below including tests, why the solution works and time 
# and space complexity: 13 minutes

# Problem: https://leetcode.com/problems/longest-common-prefix/description/ 

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if any(s == "" for s in strs):
            return ""
        idx = 0
        while idx < len(strs[0]):
            if all(idx < len(s) for s in strs[1:]):
                if all(strs[0][idx] == s[idx] for s in strs[1:]):
                    idx += 1
                else:
                    break
            else:
                break
        return strs[0][:idx] if idx > 0 else ""

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestCommonPrefix(["a"]) == "a"
    assert sol.longestCommonPrefix(["a", "abc", "hi"]) == ""
    assert sol.longestCommonPrefix(["", "abc", "hi"]) == ""
    assert sol.longestCommonPrefix(["abc", "ab", "a"]) == "a"

# Explanation: the code uses a pointer idx and if all the characters in each
# string in s at idx are equal, then idx is incremented
# Time: O(L * n), L = length of shortest string in strs, n = len(strs)
# Space: O(1)

# Learning lessons (done after completing all of above in 13 minutes):
#   - No major learning lessons



