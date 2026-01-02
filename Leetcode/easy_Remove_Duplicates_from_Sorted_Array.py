# 5:40 - 6:17

from typing import List

def remove_duplicates_from_sorted_array_in_place(nums: List[int]) -> List[int]:
    left = 0
    prev_n = nums[0]
    for right, n in enumerate(nums):
        if n != prev_n:
            nums[left:right] = [n] + ["_"] * (right - left)
            left = right
        prev_n = n






