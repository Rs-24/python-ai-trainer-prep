# Time to write all of below including tests, explanation and time and aux
# and total space: 37 mins

# Problem: https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        h = []
        for num, freq in c.items():
            heapq.heappush(h, (freq, num))
            if len(h) > k:
                heapq.heappop(h)
        return [num for freq, num in h]

if __name__ == "__main__":
    sol = Solution()
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([-1, 0, 1], 3)) == sorted([-1, 0, 1])
    result = sorted(sol.topKFrequent([-1, 0, 0, 1], 2))
    assert result in (sorted([0, -1]), sorted([0, 1]))

# Explanation: the code creates a dictionary of each element in nums and
# its frequency, then stores each frequency and number as a tuple in a
# heap and limits the heap's size to k, so that it only stores the k most
# frequent elements, and then outputs these elements
# Time: worst case: O(n + m log k), n = len(nums), m = number of
# unique elements in array
# Space: excluding output: O(m + k), worst case O(n + k)

# Bucket sort method:
from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time: O(n + m), n = len(nums), m = number of unique elements in
        # array
        # Space: excluding output: O(m + n), worst case O(n)
        c = Counter(nums)
        buckets = [[] for _ in range(len(nums))]
        for num, freq in c.items():
            buckets[freq - 1].append(num)
        out = []
        i = len(nums) - 1
        while i >= 0:
            for num in buckets[i]:
                out.append(num)
                if len(out) == k:
                    return out
            i -= 1
        return out


