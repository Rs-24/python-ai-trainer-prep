

class Solution:
    def combinationSum(self, candidates: list, target: int) -> list[list]:
        # Time: O(n log n + n^2)
        # Space: O(n^2)
        candidates.sort()
        out = []
        s = [(0, [], target)]
        while s:
            i, c, r = s.pop()
            if r == 0:
                out.append(c)
                continue
            for j in range(i, len(candidates)):
                if candidates[j] > r:
                    break
                s.append((j, c + [candidates[j]], r - candidates[j]))
        return out


