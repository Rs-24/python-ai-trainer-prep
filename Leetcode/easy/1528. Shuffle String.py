

class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        # Time: O(n), n = len(s) = len(indices)
        # Space: O(n)
        out = [""] * len(s)
        for i, ch in enumerate(s):
            out[indices[i]] = ch
        return "".join(out)


