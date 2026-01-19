# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/pascals-triangle-ii/description/

from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex <= 1:
            return [1] * (rowIndex+1)

        out = [1, 1]
        temp = []
        for i in range(2, rowIndex+1):
            temp = []
            for j in range(len(out)-1):
                temp.append(out[j] + out[j+1])
            out = [1] + temp + [1]
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.getRow(0) == [1]
    assert sol.getRow(1) == [1, 1]
    assert sol.getRow(2) == [1, 2, 1]
    assert sol.getRow(3) == [1, 3, 3, 1]
    assert sol.getRow(4) == [1, 4, 6, 4, 1]

# Explanation: Each row is calculated using the previous row until the desired
# row is found and then outputted
# Time: O(n^2), n = rowIndex
# Aux space excluding output and input: O(n)
# Total space including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 14 mins):
#   - Another method would be updating the list in place. My attempt is below: 
#
# def getRow(self, rowIndex: int) -> List[int]:
#     # Time: O(n^2), n = rowIndex
#     # Aux space excluding output and input: O(1)
#     # Total space including output, excluding input: O(n)
#     if rowIndex <= 1:
#         return [1] * (rowIndex + 1)
#     out = [1, 1]
#     for i in range(2, rowIndex+1):
#         j = len(out)-1
#         while j >= 1:
#             out[j] = out[j] + out[j-1]
#             j -= 1
#         out.append(1)
#     return out









