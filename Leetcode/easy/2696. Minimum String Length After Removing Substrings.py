

class Solution:
    def minLength(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        a = []
        for ch in s:
            if a and ((a[-1] == "A" and ch == "B") or (a[-1] == "C" and ch == "D")):
                a.pop()
                continue
            a.append(ch)
        return len(a)


