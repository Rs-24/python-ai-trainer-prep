

class Solution:
    def maskPII(self, s: str) -> str:
        # Time: O(1)
        # Space: O(1)
        if "@" in s:
            s = s.lower()
            n, d = s.split("@")
            return n[0] + "*****" + n[-1] + "@" + d
        s = "".join(ch for ch in s if ch.isdigit())
        if len(s) == 10:
            return "***-***-" + s[-4:]
        return "+" + "*" * (len(s) - 10) + "-***-***-" + s[-4:]


