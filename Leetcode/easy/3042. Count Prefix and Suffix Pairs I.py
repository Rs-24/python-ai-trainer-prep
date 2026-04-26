# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Time: O(1)
        # Space: O(1)
        n = len(words)
        count = 0
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            if str2.startswith(str1) and str2.endswith(str1):
                return True
            return False
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count


