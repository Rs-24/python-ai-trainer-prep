# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/relative-ranks/description/

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Time: O(n log n), n = len(scores)
        # Space, excluding output: O(n)
        out = [""] * len(score)
        ranked = sorted([(s, i) for i, s in enumerate(score)], reverse=True)
        place = 1
        for s, i in ranked:
            if place == 1:
                out[i] = "Gold Medal"
            elif place == 2:
                out[i] = "Silver Medal"
            elif place[i] == 3:
                out[i] = "Third Medal"
            else:
                out[i] = str(place)
            place += 1
        return out


