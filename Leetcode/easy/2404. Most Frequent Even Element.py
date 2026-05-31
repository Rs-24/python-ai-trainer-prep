

from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list) -> int:
        # Time: O(n)
        # Space: O(n)
        c = Counter(num for num in nums if num % 2 == 0)
        if not c:
            return -1
        best_freq = max(c.values())
        smallest = max(c.keys())
        for num, freq in c.items():
            if freq == best_freq and num < smallest:
                smallest = num
        return smallest


