# Time to write all of below including tests, explanation and time and aux 
# space: 19 mins

# Problem: https://leetcode.com/problems/pascals-triangle/description/

from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        
        out = [[1], [1, 1]]

        
        for i in range(numRows):
            if i+1 <= 2:
                continue
            temp_list = []

            prev = out[-1]

            for j in range(len(prev)):
                if j == len(prev)-1:
                    continue
                temp_list.append(prev[j] + prev[j+1])
            
            temp_list = [1] + temp_list + [1]

            out.append(temp_list)
        
        return out


if __name__ == "__main__":
    sol = Solution()
    assert sol.generate(1) == [[1]]
    assert sol.generate(2) == [[1], [1, 1]]
    assert sol.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert sol.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert sol.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# Explanation: the previous row is used to calculate the next row until numRows
# is reached
# Time: O(numRows^2)
# Aux space: O(numRows)

# Learning lessons (done after completing all of above in 19 mins):
#   - I could have improved my space complexity comment by saying:
#     Aux space excluding output and input: O(n), n = numRows
#     Total space including output, excluding input: O(n^2)







