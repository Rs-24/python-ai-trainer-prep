# Time to write all of below including tests, explanation and time and aux
# and total space: 1h 4 mins

# I required help from chatGPT to solve this one

# Problem: https://leetcode.com/problems/daily-temperatures/description/

from typing import List 

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        for i, t, in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                out[j] = i - j
            stack.append(i)
        return out

if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([30]) == [0]
    assert sol.dailyTemperatures([30, 40, 50, 30]) == [1, 1, 0, 0]
    assert sol.dailyTemperatures([30, 30, 30, 30]) == [0, 0, 0, 0]
    assert sol.dailyTemperatures([100, 90, 80, 80]) == [0, 0, 0, 0]

# Explanation: the code iterates through the temperatures list while keeping
# a stack of indices in decreasing temperature order, and modifies out 
# whenever the current temperature is higher than the temperature represented
# by the last index in the stack
# Time: O(n), n = len(temperatures)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)

# Learning lessons (done after completing all of above in 1h 4 mins):
#   - No major learning lessons
