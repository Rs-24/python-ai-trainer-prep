# Time to write all of below including tests, explanation and time and aux
# and total space: 3 mins

# Problem: https://leetcode.com/problems/count-square-sum-triples/description/

class Solution:
    def countTriples(self, n: int) -> int:
        # Time: O(n^2)
        # Space: O(1)
        count = 0
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                c = a * a + b * b
                c2 = int(c ** 0.5)
                if c2 <= n and c2 * c2 == c:
                    count += 1
        return count


