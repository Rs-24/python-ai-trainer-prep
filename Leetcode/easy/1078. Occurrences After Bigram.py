

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        # Time: O(n), n = len(text)
        # Space: O(n)
        out = []
        text = text.split()
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                out.append(text[i + 2])
        return out


