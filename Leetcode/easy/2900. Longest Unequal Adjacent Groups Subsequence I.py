# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/description/

from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # Time: O(n), n = len(groups) = len(words)
        # Space: O(1)
        prev = groups[0]
        out = [words[0]]
        for i in range(1, len(groups)):
            if prev != groups[i]:
                out.append(words[i])
            prev = groups[i]
        return out


