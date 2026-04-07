# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/day-of-the-year/description/

class Solution:
    def dayOfYear(self, date: str) -> int:
        # Time: O(1)
        # Space: O(1)
        year, month, day = int(date[:4]), int(date[5:7]), int(date[8:10])
        leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if leap: m[1] = 29
        total = sum(m[i] for i in range(month - 1)) + day
        return total


