# Time to write all of below including tests, why the solution works and time 
# and space complexity: 32 mins

# Problem: https://leetcode.com/problems/add-binary/description/

from typing import List, Callable

def add_binary(a: str, b: str) -> str:
    a_total = 0
    i = len(a) - 1
    while i >= 0:
        a_total += int(a[i]) * (2**(len(a) - 1 - i))
        i -= 1
    
    b_total = 0
    i = len(b) - 1
    while i >= 0:
        b_total += int(b[i]) * (2**(len(b) - 1 - i))
        i -= 1

    total = a_total + b_total
    result: List[str] = []
    two_power = 0
    while 2 ** two_power <= total:
        two_power += 1
    two_power -= 1
    while two_power >= 0:
        if total - 2 ** two_power >= 0:
            result.append("1")
            total -= 2 ** two_power
            two_power -= 1
        else:
            result.append("0")
            two_power -= 1
    return "".join(result)

def run_tests(f: Callable[[str, str], str]) -> None:
    tests = [("11", "11", "110"), ("1", "1", "10"), ("101", "101", "1010")]
    for a, b, expected in tests:
        actual = f(a, b)
        assert actual == expected, f"{f.__name__}({a!r}, {b!r}) = {actual}, expected {expected}"

def test() -> None:
    print("Running tests...")
    run_tests(add_binary)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# Why this solution works:
#   - Each number is converted to binary and summed together. Then the largest
#     power of two that can fit inside the number is calculated. Then the function
#     works back from this largest two power to build the binary number, and the 
#     string version of this number is then outputted
#
# Time complexity: O(len(a) + len(b))
# Auxiliary space complexity: O(len(a) + len(b))
#
# Learning lessons (done after completing all of above in 25 mins):
#   - I later tried a = "0" and b = "0", and the result was "" instead of "0",
#     which is incorrect. I could try and fix this bug but a better method which
#     I now realise would be to do the binary addition directly without converting
#     to decimal first. My new method is below:
# 
# def add_binary(a: str, b: str) -> str:
#     a, b = a[::-1], b[::-1]
#     if len(a) < len(b):
#         a += "0" * (len(b) - len(a))
#     elif len(a) > len(b):
#         b += "0" * (len(a) - len(b))
#     result: List[str] = []
#     carry = 0
#     for i in range(len(a)):
#         a_ch = ord(a[i]) - ord("0")
#         b_ch = ord(b[i]) - ord("0")
#         total = a_ch + b_ch + carry
#         result.append(str(total % 2))
#         carry = total // 2
#     if carry == 1:
#         result.append("1")
#     return "".join(reversed(result))




