# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-pairs-of-similar-strings/description/

from typing import List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Time: O(m * n log n), m = len(words), n = len(average word in words)
        # Space: O(m * n)
        d = {}
        ans = 0
        for word in words:
            key = "".join(sorted(set(word)))
            ans += d.get(key, 0)
            d[key] = d.get(key, 0) + 1
        return ans


