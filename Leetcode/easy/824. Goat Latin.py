

class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        # Time: O(n), n = len(sentence)
        # Space: O(n)
        s = sentence.split()
        out = []
        for i, word in enumerate(s):
            cur = []
            v = word[0] in "aeiouAEIOU"
            for j, ch in enumerate(word):
                if j == 0 and not v:
                    continue
                cur.append(ch)
            if not v:
                cur.append(word[0])
            cur.append("m")
            cur.append("a")
            for _ in range(i + 1):
                cur.append("a")
            out.append("".join(cur))
        return " ".join(out)


