# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # Time: O(1)
        # Space: O(1)
        total = (high - low) // 2
        total += 1 if low % 2 == 1 or high % 2 == 1 else 0
        return total


