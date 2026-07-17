

class Solution:
    def makesquare(self, matchsticks: list) -> bool:
        # Time: O(n log n)
        # Space: O(1)
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        matchsticks.sort(reverse=True)
        if matchsticks[0] > s // 4:
            return False
        t = [0] * 4
        def dfs(i):
            if i == len(matchsticks):
                return True
            for j in range(4):
                if t[j] + matchsticks[i] <= s // 4:
                    t[j] += matchsticks[i]
                    if dfs(i + 1):
                        return True
                    t[j] -= matchsticks[i]
                    if t[j] == 0:
                        break
            return False
        return dfs(0)


