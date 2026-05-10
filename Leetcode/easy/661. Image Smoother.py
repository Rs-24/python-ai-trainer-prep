

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        # Time: O(m * n), m = len(img), n = len(img[0])
        # Space: O(1)
        m, n = len(img), len(img[0])
        for r in range(m):
            for c in range(n):
                total = 0
                count = 0
                for dr, dc in [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]:
                    if 0 <= r + dr < m and 0 <= c + dc < n:
                        total += (img[r + dr][c + dc] & 255)
                        count += 1
                avg = (total // count) << 8
                img[r][c] |= avg
        for r in range(m):
            for c in range(n):
                img[r][c] >>= 8
        return img


