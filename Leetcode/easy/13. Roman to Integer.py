# Time to write all of below including tests, why the solution works and time 
# and space complexity: 19 minutes

# Problem: https://leetcode.com/problems/roman-to-integer/description/ 

from typing import Callable, Any

def roman_to_integer(s: str) -> int:
    total = 0
    prev_ch = s[0]
    for ch in s:        
        if ch == "I":
            total += 1
        elif ch == "V":
            if prev_ch == "I":
                total += 3
            else:
                total += 5
        elif ch == "X":
            if prev_ch == "I":
                total += 8
            else:
                total += 10
        elif ch == "L":
            if prev_ch == "X":
                total += 30
            else:
                total += 50
        elif ch == "C":
            if prev_ch == "X":
                total += 80
            else:
                total += 100
        elif ch == "D":
            if prev_ch == "C":
                total += 300
            else:
                total += 500
        elif ch == "M":
            if prev_ch == "C":
                total += 800
            else:
                total += 1000
        prev_ch = ch
    return total

def run_test(f: Callable[[str], int]) -> None:
    tests = [("XI", 11), ("MIV", 1004), ("I", 1)]
    for test, expected in tests:
        actual = f(test)
        assert actual == expected, f"{f.__name__}({test!r}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(roman_to_integer)
    print("All tests passed")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - The string s is taken in and total is incremented by the integer equivalent
#     of the current numeral. prev_ch is also stored to adjust total accordingly,
#     e.g. I increments total by 1, and if the next numeral is X, then total is 
#     then incremented by 8, not 10
# Time complexity: O(len(s))
# Space complexity: O(1)



# Learning lessons (done after completing all of above in 19 minutes):
#   - I could have added a few more tests, e.g. "IV" -> 4, "IX" -> 9,
#     "LVIII" -> 58, etc
#   - A dict of each numeral and it's corresponding value would have been
#     better, the following shows an alternative way of solving the problem
#     after now realising that:
# 
# from typing import Dict
# def roman_to_integer(s: str) -> int:
#     numerals: Dict[str, int] = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#     total = 0
#     for i, ch in enumerate(s):
#         total += numerals[ch]
#         if i > 0 and numerals[s[i - 1]] < numerals[s[i]]:
#             total -= 2 * numerals[s[i-1]]
#     return total







