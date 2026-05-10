

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Time: O(m + n)
        # Space: O(1)
        i, j, insert_pos = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[insert_pos] = nums1[i]
                i -= 1
            else:
                nums1[insert_pos] = nums2[j]
                j -= 1
            insert_pos -= 1


