

class Solution:
    def reorderSpaces(self, text: str) -> str:
        # Time: O(n), n = len(text)
        # Space: O(n)
        s = text.count(" ")
        t = text.split()
        num_spaces = len(t) - 1
        if num_spaces == 0:
            return t[0] + " " * s
        spaces = " " * (s // num_spaces)
        return spaces.join(t) + " " * (s % num_spaces)


