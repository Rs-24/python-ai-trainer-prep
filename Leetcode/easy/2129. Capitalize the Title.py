

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        # Time: O(n), n = len(title)
        # Space: O(n)
        out = []
        for w in title.split():
            if len(w) <= 2:
                out.append(w.lower())
            else:
                w = list(w.lower())
                w[0] = w[0].upper()
                out.append("".join(w))
        return " ".join(out)


