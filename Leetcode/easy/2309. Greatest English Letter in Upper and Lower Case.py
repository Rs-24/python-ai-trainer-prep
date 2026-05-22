

class Solution:
    def greatestLetter(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        s = set(s)
        for i in range(ord("z"), ord("a") - 1, -1):
            if chr(i) in s and chr(i).upper() in s:
                return chr(i).upper()
        return ""


