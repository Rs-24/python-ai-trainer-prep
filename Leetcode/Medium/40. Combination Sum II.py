

class Solution:
    def combinationSum2(self, candidates: list, target: int) -> list[list]:
        # Time: O(n log n + n^2)
        # Space: O(n^2)
        candidates.sort()
        out = []
        s = [(0, [], target)]
        while s:
            i, p, r = s.pop()
            if r == 0:
                out.append(p)
                continue
            for j in range(i, len(candidates)):
                if j > i and candidates[j - 1] == candidates[j]:
                    continue
                if candidates[j] > r:
                    break
                s.append((j + 1, p + [candidates[j]], r - candidates[j]))
        return out


