

class Solution:
    def simplifyPath(self, path: str) -> str:
        # Time: O(n)
        # Space: O(n)
        s = []
        p = path.split("/")
        for t in p:
            if t == "" or t == ".":
                continue
            elif t == "..":
                if s:
                    s.pop()
            else:
                s.append(t)
        return "/" + "/".join(s)


