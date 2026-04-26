# Time to write all of below including tests, explanation and time and aux
# and total space: 2 mins

# Problem: https://leetcode.com/problems/number-of-valid-clock-times/description/

class Solution:
    def countTime(self, time: str) -> int:
        total = 1
        i = 0
        while i < len(time):
            if time[i] == "?":
                if i == 0:
                    if time[i + 1] == "?":
                        total *= 24
                        i += 1
                    elif int(time[i + 1]) <= 3:
                        total *= 3
                    else:
                        total *= 2 
                elif i == 1:
                    if int(time[i - 1]) < 2:
                        total *= 10
                    else:
                        total *= 3
                elif i == 3:
                    total *= 6
                else:
                    total *= 10
            i += 1
        return total


