

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list:
        t = set()
        a = set()
        for i in range(len(s) - 9):
            if s[i:i + 10] in t:
                a.add(s[i:i + 10])
            else:
                t.add(s[i:i + 10])
        return list(a)


