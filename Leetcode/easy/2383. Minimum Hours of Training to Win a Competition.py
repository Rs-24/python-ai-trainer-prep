# Time to write all of below including tests, explanation and time and aux
# and total space: 1 min

# Problem: https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/

from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # Time: O(m + n), m = len(energy), n = len(experience)
        # Space: O(1)
        total = max(0, sum(energy) + 1 - initialEnergy)
        e_so_far = initialExperience
        needed = 0
        for e in experience:
            if e >= e_so_far:
                train = e - e_so_far + 1
                needed += train
                e_so_far += train
            e_so_far += e
        return total + needed


