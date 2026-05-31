

class Solution:
    def countTime(self, time: str) -> int:
        # Time: O(n)
        # Space: O(1)
        count = 1
        i = 0
        while i < len(time):
            if time[i] == "?":
                if i == 0:
                    if time[i + 1] == "?":
                        count *= 24
                        i += 1
                    elif int(time[i + 1]) <= 3:
                        count *= 3
                    else:
                        count *= 2
                elif i == 1:
                    if int(time[i - 1]) <= 1:
                        count *= 10
                    else:
                        count *= 3
                elif i == 3:
                    count *= 6
                else:
                    count *= 10
            i += 1
        return count


