# Time to write all of below including tests, explanation and time and aux 
# space: 11 mins

# Problem: https://leetcode.com/problems/pascals-triangle-ii/description/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        prev = [1, 1]
        for _ in range(2, rowIndex + 1):
            temp = []
            for i in range(len(prev) - 1):
                temp.append(prev[i] + prev[i + 1])
            temp = [1] + temp + [1]
            prev = temp
        return prev

if __name__ == "__main__":
    sol = Solution()
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1, 1]
    assert sol.getRow(2) == [1, 2, 1]
    assert sol.getRow(3) == [1, 3, 3, 1]
    assert sol.getRow(4) == [1, 4, 6, 4, 1]
    assert sol.getRow(5) == [1, 5, 10, 10, 5, 1]

# Explanation: the code stores the previous row in prev, and calculates each
# next row until it reaches rowIndex. It calculates each row by creating a new
# list consisting of the sum of the consecutive elements in prev and appending
# 1 on either side to form the new row
# Time: O(n^2), n = rowIndex
# Space: O(n)

# Learning lessons (done after completing all of above in 11 mins):
#   - Another method would be updating the list in place. My attempt is below:
#
# def getRow(self, rowIndex: int) -> List[int]:
#     # Time: O(n^2), n = rowIndex
#     # Space: O(1) extra space, O(n) output space
#     if rowIndex == 0:
#         return [1]
#     elif rowIndex == 1:
#         return [1, 1]
#     prev = [1, 1]
#     for _ in range(2, rowIndex + 1):
#         i = len(prev) - 1
#         while i >= 1:
#             prev[i] += prev[i - 1]
#             i -= 1
#         prev += [1]
#     return prev










