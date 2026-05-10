

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # Time: O(n), n = len(strs)
        # Aux space: O(1) 
        i = 0
        while i < min(len(s) for s in strs):
            if not all(strs[0][i] == s[i] for s in strs):
                break
            i += 1
        return strs[0][:i]


