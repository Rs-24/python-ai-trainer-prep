

from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Time: O(n log n)
        # Space: O(n)
        return "".join([ch * f for ch, f in sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)])


