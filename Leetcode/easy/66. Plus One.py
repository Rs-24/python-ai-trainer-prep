# Time to write all of below including tests, why the solution works and time 
# and space complexity: 19 mins

# Problem: https://leetcode.com/problems/plus-one/description/

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        new = 0
        i = len(digits) - 1
        while i >= 0:
            if i == len(digits) - 1:
                new = digits[i] + 1 + carry
            else:
                new = digits[i] + carry
            digits[i] = new % 10
            carry = new // 10
            i -= 1
        return [1] + digits if carry > 0 else digits 

if __name__ == "__main__":
    sol = Solution()
    assert sol.plusOne([9]) == [1, 0]
    assert sol.plusOne([1, 9]) == [2, 0]
    assert sol.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert sol.plusOne([1, 9, 1]) == [1, 9, 2]
    assert sol.plusOne([9, 0, 0]) == [9, 0, 1]
    assert sol.plusOne([1, 2, 3]) == [1, 2, 4]

# Explanation: the code iterates through digits from the end and modifies each
# digit while storing carry and altering carry accordingly. Once the loop ends,
# if carry is greater than 0, then [1] + digits is returned, otherwise just
# digits is returned
# Time: O(n), n = len(digits)
# Aux space, excluding output and input: O(1)
# Total space, including output, excluding input: O(n)
    

