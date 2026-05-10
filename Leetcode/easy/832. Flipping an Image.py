

class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        # Time: O(m * n), m = len(image), n = len(image[0])
        # Space: O(1)
        m, n = len(image), len(image[0])
        for row in range(m):
            l, r = 0, n - 1
            while l < r:
                image[row][l] ^= 1
                image[row][r] ^= 1
                image[row][l], image[row][r] = image[row][r], image[row][l]
                l += 1
                r -= 1
            if len(image[row]) % 2 != 0:
                image[row][n // 2] ^= 1 
        return image


