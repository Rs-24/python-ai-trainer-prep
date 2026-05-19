

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # Time: O(n), n = len(word)
        # Space: O(n)
        s = set()
        cur = []
        for ch in word:
            if ch.isdigit():
                cur.append(ch)
            else:
                if len(cur) > 0:
                    s.add(int("".join(cur)))
                    cur = []
        if len(cur) > 0:
            s.add(int("".join(cur)))
        return len(s)


