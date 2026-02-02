# Time to write all of below including tests, explanation and time and aux
# and total space: 30 mins

# Problem: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

from typing import List
from math import floor

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch in "+-/*":
                b = stack.pop()
                a = stack.pop()
                match ch:
                    case "+":
                        stack.append(a+b)
                    case "-":
                        stack.append(a-b)
                    case "*":
                        stack.append(a*b)
                    case "/":
                        stack.append(floor(a/b))
            else:
                stack.append(int(ch))
        return stack[-1]

if __name__ == "__main__":
    sol = Solution()
    assert sol.evalRPN(["1"]) == 1
    assert sol.evalRPN(["0"]) == 0
    assert sol.evalRPN(["-1"]) == -1
    assert sol.evalRPN(["2", "1", "+"]) == 3
    assert sol.evalRPN(["2", "0", "*", "1", "2", "+", "*"]) == 0
    assert sol.evalRPN(["2", "3", "-", "1", "2", "-", "*"]) == 1
    assert sol.evalRPN(["2", "3", "4", "-", "+"]) == 1

# Explanation: the code uses a stack to process each subexpression, and
# returns the last item left in the stack
# Time: O(n), n = len(tokens)
# Aux space, excluding output and input: O(k), k = number of numbers in tokens
# Total space, including output, excluding input: O(k)

# Learning lessons (done after completing all of above in 30 mins):
#   - I now realise the line 'stack.append(floor(a/b))' doesn't actually
#     truncate towards zero, instead it should be changed to:
# stack.append(int(a/b))










