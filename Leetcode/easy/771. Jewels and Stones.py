

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Time: O(m + n), m = len(jewels), n = len(stones)
        # Space: O(m)
        j = set(jewels)
        return sum(1 for s in stones if s in j)


