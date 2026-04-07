# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/

from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # Time: O(n), n = len(salary)
        # Space: O(1)
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)


