

class Solution:
    def isValid(self, s: str) -> bool:
        # Time: O(n)
        # Space: O(n)
        t = []
        for ch in s:
            t.append(ch)
            if len(t) >= 3 and t[-3] == "a" and t[-2] == "b" and t[-1] == "c":
                for _ in range(3):
                    t.pop()
        return len(t) == 0


