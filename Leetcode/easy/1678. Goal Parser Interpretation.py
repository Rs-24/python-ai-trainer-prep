# Time to write all of below including tests, explanation and time and aux
# and total space: 4 mins

# Problem: https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        # Time: O(n), n = len(command)
        # Space: O(n)
        stack = []
        for ch in command:
            if ch == "G":
                stack.append(ch)
            elif ch == ")":
                if stack[-1] == "(":
                    stack[-1] = "o"
                else:
                    l = stack.pop()
                    a = stack.pop()
                    stack.pop()
                    stack.append(a)
                    stack.append(l)
            else:
                stack.append(ch)
        return "".join(stack)


