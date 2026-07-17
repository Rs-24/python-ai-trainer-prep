

class Solution:
    def findLongestWord(self, s: str, dictionary: list) -> str:
        # Time: O(n)
        # Space: O(1)
        def c(t: str):
            i = j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t)
        a = -1
        for i, t in enumerate(dictionary):
            if c(t):
                a = i if a == -1 or len(t) > len(dictionary[a]) or (len(t) == len(dictionary[a]) and t < dictionary[a]) else a
        return dictionary[a] if a != -1 else ""


