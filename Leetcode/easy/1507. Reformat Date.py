# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/reformat-date/description/

class Solution:
    def reformatDate(self, date: str) -> str:
        # Time: O(n), n = len(date)
        # Space: O(1)
        day, month, year = date.split()
        months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
        month = months[month]
        day = day[:-2]
        if len(day) == 1:
            day = "0" + day
        return year + "-" + month + "-" + day


