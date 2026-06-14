

class Solution:
    def kthCharacter(self, k: int) -> str:
        # Time: O(k)
        # Space: O(k)
        w = ["a"]
        while len(w) < k:
            t = []
            for ch in w:
                t.append(chr((ord(ch) - ord("a") + 1) % 26 + ord("a")))
            w.extend(t)
        return w[k - 1]


