# Time to write all of below including tests, explanation and time and aux
# and total space: 14 mins

# Problem: https://leetcode.com/problems/next-greater-element-i/description/

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n * m), n = len(nums1), m = len(nums2)
        # Space, excluding output: O(1)
        out = []
        for i, num1 in enumerate(nums1):
            found = False
            for num2 in nums2:
                if num1 == num2:
                    found = True
                elif found and num2 > num1:
                    out.append(num2)
                    break
            if len(out) < i + 1:
                out.append(-1)
        return out

# Stack method:
from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Time: O(n + m), n = len(nums1), m = len(nums2)
        # Space, excluding output: O(m)
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        for num in nums1:
            if num not in next_greater:
                next_greater[num] = -1
        return [next_greater[num] for num in nums1]


