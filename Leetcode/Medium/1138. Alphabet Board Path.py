

class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # Time: O(n)
        # Space: O(n)
        r, c, a = 0, 0, []
        for ch in target:
            x, y = (ord(ch) - ord("a")) // 5, (ord(ch) - ord("a")) % 5 
            if ch == "z":
                while y < c:
                    a.append("L")
                    c -= 1
                while x < r:
                    a.append("D")
                    r += 1
            else:
                while r < x:
                    a.append("D")
                    r += 1
                while r > x:
                    a.append("U")
                    r -= 1
                while c < y:
                    a.append("R")
                    c += 1
                while c > y:
                    a.append("L")
                    c -= 1
            a.append("!")
        return "".join(a)


