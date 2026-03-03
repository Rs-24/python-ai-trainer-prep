# Time to write all of below including tests, explanation and time and aux 
# space: 12 mins

# Problem: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if (len(stack) > 0) and (stack[-1] == pairs[ch]):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
    
if __name__ == "__main":
    sol = Solution()
    assert sol.isValid("[") == False
    assert sol.isValid(")") == False
    assert sol.isValid("()") == True
    assert sol.isValid("(){}[]") == True
    assert sol.isValid("([{}])") == True
    assert sol.isValid("((])]") == False

# Explanation: the code uses a stack to store each open parenthesis and
# compares every close parenthesis to the last element of the stack. If they
# don't correspond, then False is returned. Once the loop ends, the code
# returns True if stack is empty, and False otherwise
# Time: O(n), n = len(s)
# Aux space, excluding output and input: worst case O(n) if stack only
# consists of open parentheses
# Total space, including output, excluding input: worst case O(n) 


