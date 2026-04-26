# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # Time: O(1)
        # Space: O(1)
        cycle = 2 * (n - 1)
        position = k % cycle
        return position if position < n else cycle - position


