

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Time: O(1)
        # Space: O(1)
        return str(bin(int(date[:4]))[2:]) + "-" + str(bin(int(date[5:7]))[2:]) + "-" + str(bin(int(date[8:10]))[2:])


