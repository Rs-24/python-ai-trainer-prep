

class Solution:
    def clearDigits(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        a = []
        for ch in s:
            if ch.isdigit():
                if a:
                    a.pop()
            else:
                a.append(ch)
        return "".join(a)


