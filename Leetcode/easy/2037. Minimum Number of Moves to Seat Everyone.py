

class Solution:
    def minMovesToSeat(self, seats: list, students: list) -> int:
        # Time: O(n log n), n = len(seats) = len(students)
        # Space: O(1)
        seats.sort()
        students.sort()
        return sum(abs(se - st) for se, st in zip(seats, students))


