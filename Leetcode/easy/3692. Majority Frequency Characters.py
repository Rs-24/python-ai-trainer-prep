# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/majority-frequency-characters/description/

from collections import Counter, defaultdict

class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        # Time: O(n), n = len(s)
        # Space: O(n)
        c = Counter(s)
        d = defaultdict(list)
        for ch, freq in c.items():
            d[freq].append(ch)
        majority = max(len(chars) for chars in d.values())
        best_freq = None
        ans = []
        for freq, chars in d.items():
            if len(chars) == majority:
                if not ans:
                    ans[:] = chars
                    best_freq = freq
                else:
                    if freq > best_freq:
                        best_freq = freq
                        ans[:] = chars
        return "".join(ans)


