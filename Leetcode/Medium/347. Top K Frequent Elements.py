# Time to write all of below including tests, explanation and time and aux
# and total space: 37 mins

# Problem: https://leetcode.com/problems/top-k-frequent-elements/description/

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        out = []
        done = []
        for _ in range(k):
            best_freq = 0
            best_num = None
            for num in d:
                if best_num is None and num not in done:
                    best_num = num
                    best_freq = d[num]
                else:
                    if d[num] > best_freq and num not in done:
                        best_freq = d[num]
                        best_num = num
            out.append(best_num)
            done.append(best_num)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.topKFrequent([1], 1) == [1]
    assert sorted(sol.topKFrequent([-1, 0, 1], 3)) == sorted([-1, 0, 1])
    assert sorted(sol.topKFrequent([-1, 0, 0, 1], 2)) == sorted([0, -1]) or sorted([0, 1])

# Explanation: the code creates a dictionary of each number and its frequency, 
# and then iterates over the dictionary k times to output the k most frequent
# elements
# Time: O(n * k), n = len(nums)
# Aux space, excluding output and input: O(m), m = number of unique elements
# Total space, including output, excluding input: O(m)






    
