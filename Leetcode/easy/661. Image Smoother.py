# Time to write all of below including tests, explanation and time and aux
# and total space: 12 mins

# Problem: https://leetcode.com/problems/image-smoother/description/

from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n), m = len(img), n = len(img[0])
        # Space, excluding output: O(1)
        m, n = len(img), len(img[0])
        out = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for di, dj in [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]:
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        total += img[i + di][j + dj]
                        count += 1
                out[i][j] = total // count
        return out

# Mutating in-place version:
from typing import List     
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # Time: O(m * n), m = len(img), n = len(img[0])
        # Space: O(1)
        m, n = len(img), len(img[0])
        for i in range(m):
            for j in range(n):
                total = 0
                count = 0
                for di, dj in [(0, 0), (0, -1), (0, 1), (-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1)]:
                    if 0 <= i + di < m and 0 <= j + dj < n:
                        total += (img[i + di][j + dj] & 255)
                        count += 1
                avg = (total // count) << 8
                img[i][j] |= avg
        for i in range(m):
            for j in range(n):
                img[i][j] >>= 8
        return img


