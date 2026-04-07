# Time to write all of below including tests, explanation and time and aux
# and total space: 8 mins

# Problem: https://leetcode.com/problems/number-of-days-between-two-dates/description/

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Time: O(1)
        # Space: O(1)
        def get_days(y: int, m: int, d: int) -> int:
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
                months[1] = 29
            y -= 1
            while y >= 1971:
                d += 366 if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0) else 365
                y -= 1
            d += sum(months[:m - 1])
            return d
        y1, m1, d1 = int(date1[:4]), int(date1[5:7]), int(date1[8:10])
        y2, m2, d2 = int(date2[:4]), int(date2[5:7]), int(date2[8:10])
        return abs(get_days(y1, m1, d1) - get_days(y2, m2, d2))


