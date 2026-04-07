# Time to write all of below including tests, explanation and time and aux
# and total space: 6 mins

# Problem: https://leetcode.com/problems/day-of-the-week/description/

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Time: O(month + year - 1971)
        # Space: O(1)
        y = year
        year -= 1
        while year >= 1971:
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                day += 366
            else:
                day += 365
            year -= 1
        month -= 1
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0): months[1] = 29
        while month >= 1:
            day += months[month - 1]
            month -= 1
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return days[day % 7]


