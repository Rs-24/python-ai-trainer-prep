

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Time: O(n), n = len(flowerbed)
        # Space: O(1)
        prev = 0
        count = 0
        for i, f in enumerate(flowerbed):
            if f == 1:
                prev = 1
            else:
                if i == len(flowerbed) - 1 or flowerbed[i + 1] == 0:
                    if prev == 0:
                        count += 1
                        prev = 1
                    else:
                        prev = 0
        return count >= n


