# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/description/

from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # Time: O(m + n), m = len(nums1), n = len(nums2)
        # Aux space: O(1)
        i, j = 0, 0
        out = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                out.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                out.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                out.append([nums2[j][0], nums2[j][1]])
                j += 1
        while i < len(nums1):
            out.append([nums1[i][0], nums1[i][1]])
            i += 1
        while j < len(nums2):
            out.append([nums2[j][0], nums2[j][1]])
            j += 1
        return out


