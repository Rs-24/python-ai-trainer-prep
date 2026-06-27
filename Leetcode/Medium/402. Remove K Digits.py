

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Time: O(n)
        # Space: O(n)
        s = []
        for d in num:
            while k > 0 and s and s[-1] > d:
                s.pop()
                k -= 1
            s.append(d)
        while k > 0:
            s.pop()
            k -= 1
        a = "".join(s).lstrip("0")
        return a if a else "0"


