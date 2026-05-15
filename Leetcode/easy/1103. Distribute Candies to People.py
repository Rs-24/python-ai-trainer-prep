

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        # Time: O(candies + num_people)
        # Space: O(num_people)
        out = [0] * num_people
        i = 0
        cur = 1
        while candies > 0:
            out[i % num_people] += min(cur, candies)
            candies -= min(cur, candies)
            i += 1
            cur += 1
        return out


