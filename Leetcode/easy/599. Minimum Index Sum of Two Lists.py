# Time to write all of below including tests, explanation and time and aux
# and total space: 9 mins

# Problem: https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        # Time: O(m + n), m = len(list1), n = len(list2)
        # Space, excluding output: O(m)
        d = {word: i for i, word in enumerate(list1)}
        minimum = float("inf")
        out = []
        for i, word in enumerate(list2):
            if word in d:
                if i + d[word] < minimum:
                    out = [word]
                    minimum = i + d[word]
                elif i + d[word] == minimum:
                    out.append(word)
        return out


