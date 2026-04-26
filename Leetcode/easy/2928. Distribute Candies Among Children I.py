# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/distribute-candies-among-children-i/description/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # Time: O(1)
        # Space: O(1)
        count = 0
        for child1 in range(min(n, limit) + 1):
            for child2 in range(min(limit, n - child1) + 1):
                child3 = n - child1 - child2
                if 0 <= child3 <= limit:
                    count += 1
        return count


