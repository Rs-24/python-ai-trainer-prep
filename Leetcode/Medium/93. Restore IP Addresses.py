

class Solution:
    def restoreIpAddresses(self, s: str) -> list:
        # Time: O(n)
        # Space: O(n)
        def valid_part(a: str) -> bool:
            if len(a) > 1 and a[0] == "0":
                return False
            return int(a) <= 255
        out = []
        n = len(s)
        a = [(0, [])]
        while a:
            i, p = a.pop()
            if len(p) == 4:
                if i == n:
                    out.append(".".join(p))
                continue
            for d in range(1, 4):
                if i + d <= n and valid_part(s[i:i + d]):
                    a.append((i + d, p + [s[i:i + d]]))
        return out


