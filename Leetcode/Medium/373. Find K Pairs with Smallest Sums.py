

import heapq

class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list[list]:
        # Time: O(k log(min(k, len(nums1))))
        # Space: O(min(k, len(nums1)))
        if not nums1 or not nums2 or k == 0:
            return []
        h = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))
        a = []
        while h and len(a) < k:
            _, i, j = heapq.heappop(h)
            a.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
        return a
 

