# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Time: O(m + n), m = len(students), n = len(sandwiches)
        # Space: O(1)
        count = [0, 0]
        for student in students:
            count[student] += 1
        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                break
        return count[0] + count[1]


