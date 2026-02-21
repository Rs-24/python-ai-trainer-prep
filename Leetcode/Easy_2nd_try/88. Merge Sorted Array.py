# Time to write all of below including tests, why the solution works and time 
# and space complexity: 52 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/merge-sorted-array/description/

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if m == 0 and n == 0:
            nums1[:] = []
        elif m == 0:
            nums1[:] = nums2

        i, j = m - 1, n - 1
        insert_pos = m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[insert_pos] = nums1[i]
                i -= 1
            else:
                nums1[insert_pos] = nums2[j]
                j -= 1
            insert_pos -= 1
        
        while j >= 0:
            nums1[insert_pos] = nums2[j]
            insert_pos -= 1
            j -= 1

if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [0, 0]
    nums2 = [1, 2]   
    sol.merge(nums1, 0, nums2, 2)
    assert nums1 == [1, 2]
        
    nums1 = [1, 2]
    nums2 = []
    sol.merge(nums1, 2, nums2, 0)
    assert nums1 == [1, 2]
    
    nums1 = [1, 2, 3, 0, 0]
    nums2 = [1, 3]
    sol.merge(nums1, 3, nums2, 2)
    assert nums1 == [1, 1, 2, 3, 3]
    
    nums1 = [-1, 0, 1, 0]
    nums2 = [-2]
    sol.merge(nums1, 3, nums2, 1)
    assert nums1 == [-2, -1, 0, 1]
    
# Explanation: the code iterates through both lists from the end while using 
# insert_pos to change nums1 in-place
# Time: O(m + n)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(1)

# Learning lessons (done after completing all of above in 52 mins):
#   - No major learning lessons




