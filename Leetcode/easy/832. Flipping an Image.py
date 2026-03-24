# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/flipping-an-image/description/

from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        # Time: O(n^2), n = len(image) = len(image[0])
        # Space: O(n)
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] ^= 1
            image[i] = image[i][::-1]
        return image


