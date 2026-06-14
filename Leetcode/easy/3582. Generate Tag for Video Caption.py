

class Solution:
    def generateTag(self, caption: str) -> str:
        # Time: O(n)
        # Space: O(n)
        w = caption.split()
        out = []
        for p in w:
            p = "".join(ch for ch in p if ch.isalpha())
            if not p:
                continue
            if not out:
                out.append(p.lower())
            else:
                out.append(p.capitalize())
        return ("#" + "".join(out))[:100]


