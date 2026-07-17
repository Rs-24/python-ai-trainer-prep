

class Solution:
    def letterCasePermutation(self, s: str) -> list:
        # Time: O(n)
        # Space: O(n)
        a = []
        t = []
        def dfs(i):
            if i == len(s):
                a.append("".join(t))
                return
            if s[i].isdigit():
                t.append(s[i])
                dfs(i + 1)
                t.pop()
            else:
                t.append(s[i].lower())
                dfs(i + 1)
                t.pop()
                t.append(s[i].upper())
                dfs(i + 1)
                t.pop()
        dfs(0)
        return a


