# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/rings-and-rods/description/

class Solution:
    def countPoints(self, rings: str) -> int:
        # Time: O(n), n = len(rings)
        # Space: O(1)
        rods = [set() for _ in range(10)]
        for i in range(0, len(rings), 2):
            rods[int(rings[i + 1])].add(rings[i])        
        return sum(1 for r in rods if len(r) == 3)


