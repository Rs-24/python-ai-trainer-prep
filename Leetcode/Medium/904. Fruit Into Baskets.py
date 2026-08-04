

class Solution:
    def totalFruit(self, fruits: list) -> int:
        # Time: O(n)
        # Space: O(n)
        d = {}
        l = a = 0
        for r in range(len(fruits)):
            d[fruits[r]] = d.get(fruits[r], 0) + 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1
            a = max(a, r - l + 1)
        return a


        