# Time to write all of below including tests, explanation and time and aux
# and total space: 3 min

# Problem: https://leetcode.com/problems/time-needed-to-buy-tickets/description/

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # Time: O(n * tickets[k]), n = len(tickets)
        # Space: O(1)
        time_taken = 0
        i = 0
        while tickets[k] > 0:
            if tickets[i] == 0:
                i += 1
                if i == len(tickets):
                    i = 0
                continue
            tickets[i] -= 1
            time_taken += 1
            i += 1
            if i == len(tickets):
                i = 0
        return time_taken


