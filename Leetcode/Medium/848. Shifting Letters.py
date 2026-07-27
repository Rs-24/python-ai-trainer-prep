

class Solution:
    def shiftingLetters(self, s: str, shifts: list) -> str:
        # Time: O(n)
        # Space: O(n)
        s, t = list(s), 0
        for i in range(len(s) - 1, -1, -1):
            t = (t + shifts[i]) % 26
            s[i] = chr(ord("a") + (ord(s[i]) - ord("a") + t) % 26)
        return "".join(s)


        