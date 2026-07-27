

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Time: O(n)
        # Space: O(n)
        a = list("L" + dominoes + "R")
        l = 0
        for r in range(1, len(a)):
            if a[r] == ".":
                continue
            if r - l > 1:
                if a[l] == a[r]:
                    for i in range(l + 1, r):
                        a[i] = a[l]
                elif a[l] == "R" and a[r] == "L":
                    for i in range(1, (r - l) // 2 + 1):
                        a[l + i] = "R"
                        a[r - i] = "L"
            l = r
        return "".join(a[1:-1])


        