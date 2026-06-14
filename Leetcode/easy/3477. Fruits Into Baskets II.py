

class Solution:
    def numOfUnplacedFruits(self, fruits: list, baskets: list) -> int:
        # Time: O(n^2)
        # Space: O(n)
        used = [False] * len(baskets)
        p = 0
        for f in fruits:
            for i in range(len(used)):
                if not used[i] and f <= baskets[i]:
                    used[i] = True
                    p += 1
                    break
        return len(fruits) - p


