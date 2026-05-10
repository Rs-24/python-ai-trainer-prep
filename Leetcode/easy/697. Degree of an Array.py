

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        # Time: O(n), n = len(nums)
        # Space: O(n)
        first = {}
        last = {}
        freqs = {}
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freqs[num] = freqs.get(num, 0) + 1
        max_freq = max(freqs.values())
        best = len(nums)
        for num, freq in freqs.items():
            if freq == max_freq:
                best = min(best, last[num] - first[num] + 1)
        return best


