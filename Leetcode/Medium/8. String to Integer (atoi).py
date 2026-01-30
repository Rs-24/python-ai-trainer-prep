# Time to write all of below including tests, explanation and time and aux
# and total space: 28 mins

# Problem: https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        negative = False
        num = []
        for i, ch in enumerate(s.strip()):
            if ch == "-" and i == 0:
                negative = True
            elif ch == "+" and i == 0:
                negative = False
            elif ch in "123456789":
                num.append(ch)
            elif ch == "0":
                continue
            else:
                break
        num = int("".join(num)) if num else 0
        if num == 0:
            return 0
        num = num * -1 if negative else num
        if num < -(2**31):
            num = -(2**31)
        elif num > 2**31 - 1:
            num = 2**31 - 1
        return num

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
    
# Explanation: the program strips leading whitespace from s and iterates
# through the result. If it starts with + or -, then negative is adjusted
# accordingly, and if ch is a digit from 1-9, then appends it to num, if
# it's 0, then it continues and if none of these conditions hold it breaks
# Then num is combined to form an integer and is returned if it is 0. Then
# it is made negative if necessary and rounded to within the bounds if
# necessary. Then it is returned.
# Time: O(n), n = len(s)
# Aux space, excluding output and input: O(n)
# Total space, including output, excluding input: O(n)


def myAtoi(self, s: str) -> int:

    negative = False

    n = 0

    for i, d in enumerate(s):
        if d in "+-":
            if i == 0:
                if d == "-":
                    negative = True
            else:
                break
        elif d in "123456789":
            n = n * 10 + int(d)
        elif d == 0:
            if n == 0:
                continue
            else:
                n *= 10
        else:
            break
    
    


        
















