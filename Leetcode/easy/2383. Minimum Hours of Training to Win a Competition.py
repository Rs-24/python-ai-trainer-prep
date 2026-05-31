

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: list, experience: list) -> int:
        # Time: O(n)
        # Space: O(1)
        total = max(0, sum(energy) + 1 - initialEnergy)
        needed = 0
        e_so_far = initialExperience
        for e in experience:
            if e >= e_so_far:
                train = e - e_so_far + 1
                needed += train
                e_so_far += train
            e_so_far += e
        return total + needed


