# Time to write all of below including tests, why the solution works and time 
# and space complexity: 25 mins

# Problem: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h = len(haystack)
        n = len(needle)
        if h < n:
            return -1
        elif h == n:
            return 0 if haystack == needle else -1
        for i in range(h - n + 1):
            if haystack[i:i+n] == needle:
                return i
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

# Time: O((h - n + 1) * n), h = len(haystack), n = len(needle)
# Space: O(n)






