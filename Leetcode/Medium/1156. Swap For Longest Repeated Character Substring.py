

from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Time: O(n)
        # Space: O(1)
        c, a, i = Counter(text), 0, 0
        while i < len(text):
            j = i
            while j < len(text) and text[j] == text[i]:
                j += 1
            a = max(a, min(j - i + 1, c[text[i]]))
            k = j + 1
            while k < len(text) and text[k] == text[i]:
                k += 1
            a = max(a, min(k - i, c[text[i]]))
            i = j
        return a


