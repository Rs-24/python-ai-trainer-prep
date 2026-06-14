

from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(s)
        m_v = max(f for ch, f in c.items() if ch in "aeiou") if any(ch in "aeiou" for ch in s) else 0
        m_c = max(f for ch, f in c.items() if ch not in "aeiou") if any(ch not in "aeiou" for ch in s) else 0
        return m_v + m_c


