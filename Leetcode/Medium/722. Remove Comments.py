

class Solution:
    def removeComments(self, source: list) -> list:
        # Time: O(n)
        # Space: O(n)
        a = []
        in_block = False
        t = []
        for s in source:
            i = 0
            if not in_block:
                t = []
            while i < len(s):
                if in_block:
                    if i + 1 < len(s) and s[i:i + 2] == "*/":
                        in_block = False
                        i += 1
                    i += 1
                else:
                    if i + 1 < len(s) and s[i:i + 2] == "/*":
                        in_block = True
                        i += 2
                    elif i + 1 < len(s) and s[i:i + 2] == "//":
                        break
                    else:
                        t.append(s[i])
                        i += 1
            if not in_block and t:
                a.append("".join(t))
        return a


