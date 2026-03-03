# Time to write all of below including tests, explanation and time and aux
# and total space: 28 mins

# Problem: https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        num = None
        sign = None
        limit = 2**31 - 1
        i = 0
        while i < len(s):
            if s[i] == " ":
                if num is not None:
                    break
            elif s[i] in "+-":
                if num is not None or sign is not None:
                    break
                if sign is None:
                    sign = 1 if s[i] == "+" else -1
                    if sign == -1:
                        limit += 1
            elif s[i] in "0123456789":
                if num is None:
                    num = int(s[i])
                else:
                    if num > (limit - int(s[i])) // 10:
                        num = limit
                        break
                    num = num * 10 + int(s[i])
            else:
                break
            i += 1
        if num is None or num == 0:
            return 0
        sign = 1 if sign is None else sign
        return num * sign

if __name__ == "__main__":
    sol = Solution()
    assert sol.myAtoi("") == 0
    assert sol.myAtoi("a") == 0
    assert sol.myAtoi("aA1") == 0
    assert sol.myAtoi("1231a") == 1231
    assert sol.myAtoi("9") == 9
    assert sol.myAtoi("-8") == -8
    assert sol.myAtoi("+7") == 7
    assert sol.myAtoi("0-1") == 0
    assert sol.myAtoi("0") == 0
    assert sol.myAtoi(" ") == 0
    assert sol.myAtoi("9 ") == 9
    assert sol.myAtoi(" 9") == 9
    assert sol.myAtoi("4.5") == 4
    assert sol.myAtoi("-4.5") == -4
    assert sol.myAtoi("4.5 ") == 4
    assert sol.myAtoi("4 ") == 4
    
# Explanation: the program iterates through s, while building num and sign by
# skipping whitespace, analysing any digits or signs, and breaking the loop
# when appropriate
# Time: O(k), k = number of characters encountered, worst case O(n),
# n = len(s)
# Space: O(1)


