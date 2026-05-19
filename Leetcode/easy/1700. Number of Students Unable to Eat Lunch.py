

class Solution:
    def countStudents(self, students: list, sandwiches: list) -> int:
        # Time: O(m + n), m = len(students), n = len(sandwiches)
        # Space: O(1)
        c = [0, 0]
        for s in students:
            c[s] += 1
        for s in sandwiches:
            if c[s] > 0:
                c[s] -= 1
            else:
                break
        return sum(c)


