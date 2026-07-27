

class Solution:
    def flipgame(self, fronts: list, backs: list) -> int:
        # Time: O(n)
        # Space: O(n)
        s = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                s.add(fronts[i])
        a = float("inf")
        for i in range(len(fronts)):
            if fronts[i] not in s:
                a = min(a, fronts[i])
            if backs[i] not in s:
                a = min(a, backs[i])
        return 0 if a == float("inf") else a


