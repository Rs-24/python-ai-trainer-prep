# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/maximum-height-of-a-triangle/description/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # Time: O(n), n = red + blue
        # Space: O(1)
        def build(r: int, b: int) -> int:
            row_size = 1
            cur = "r"
            while True:
                if cur == "r":
                    if r < row_size:
                        break
                    r -= row_size
                    cur = "b"
                else:
                    if b < row_size:
                        break
                    b -= row_size
                    cur = "r"
                row_size += 1
            return row_size - 1
        return max(build(red, blue), build(blue, red))


