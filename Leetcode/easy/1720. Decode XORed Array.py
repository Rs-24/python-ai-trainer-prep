

class Solution:
    def decode(self, encoded: list, first: int) -> list:
        # Time: O(n), n = len(encoded)
        # Space: O(n)
        out = [first]
        for num in encoded:
            out.append(out[-1] ^ num)
        return out


