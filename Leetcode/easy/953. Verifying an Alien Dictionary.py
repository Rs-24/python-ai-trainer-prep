# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/verifying-an-alien-dictionary/description/

from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Time: O(m + n), m = len(order), n = total number of characters in
        # words
        # Space: O(m)
        rank = {ch: i for i, ch in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
            else:
                if len(w1) > len(w2):
                    return False
        return True


