

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # Time: O(n ** 0.5)
        # Space: O(1)
        def build(r: int, b: int) -> int:
            l = 1
            cur = "r"
            while True:
                if cur == "r":
                    if r < l:
                        break
                    r -= l
                    cur = "l"
                else:
                    if b < l:
                        break
                    b -= l
                    cur = "r"
                l += 1
            return l - 1
        return max(build(red, blue), build(blue, red))


