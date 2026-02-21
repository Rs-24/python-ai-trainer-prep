# Time to write all of below including tests, explanation and time and aux 
# space: 14 mins

# Problem: https://leetcode.com/problems/pascals-triangle/description/

from typing import List 

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        out = [[1], [1, 1]]
        prev = [1, 1]
        temp = []
        for row in range(3, numRows + 1):
            temp = []
            for i in range(len(prev) - 1):
                temp.append(prev[i] + prev[i + 1])
            temp = [1] + temp + [1]
            out.append(temp)
            prev = temp
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]
    assert sol.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert sol.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert sol.generate(6) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]

# Explanation: the code stores the previous row as prev, and sums together 
# consecutive elements in prev to form a new list. It then appends a 1 to 
# either side to form the row, and appends this to out before moving on to
# the next row to calculate
# Time: O(n^2), n = numRows
# Space: O(n) excluding output

# Learning lessons (done after completing all of above in 14 mins):
#   - No major learning lessons



