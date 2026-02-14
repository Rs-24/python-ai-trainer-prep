# 2

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        i = len(digits) - 1























































# # Time to write all of below including tests, why the solution works and time 
# # and space complexity: 25 mins

# # Problem: https://leetcode.com/problems/plus-one/description/

# from typing import List, Callable

# def plus_one(digits: List[int]) -> List[int]:
#     if not digits:
#          return digits
#     carry_one = False
#     if digits[-1] == 9:
#             carry_one = True
#             digits[-1] = 0
#     else:
#         digits[-1] += 1
#         return digits
#     index = len(digits) - 2
#     while carry_one:
#         if index == 0:
#              digits[0] = 1
#              digits.append(0)
#              break    
#         if digits[index] == 9:
#             digits[index] = 0
#             carry_one = True
#             index -= 1
#         else:
#             digits[index] += 1
#             break
#     return digits

# def run_tests(f: Callable[[List[int]], List[int]]) -> None:
#      tests = [([1, 2, 3], [1, 2, 4]), ([9, 9, 9], [1, 0, 0, 0]), ([1, 9], [2, 0]), ([], []), ([1], [2])]
#      for test, expected in tests:
#           actual = f(expected)
#           assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

# def test() -> None:
#      print("Running tests...")
#      run_tests(plus_one)
#      print("All tests passed!")

# if __name__ == "__main__":
#      test()

# # Why this solution works:
# #   - If digits is empty, then digits itself is returned as is. Otherwise the last
# #     digit is incremented and if there is a carry_one then the while loop begins
# #     until carry_one is false. Within the while loop and each previous digit is 
# #     incremented by 1 until there are no more carry on's. If the first digit 
# #     is reached and there is still a carry one, then the first digit is set to 1,
# #     every remaining digit is set to 0 and another 0 is appended. Once the for  
# #     loop ends, the resulting list is returned
# #
# # Time complexity: O(len(digits))
# # Space complexity: O(1)


# # Learning lessons (done after completing all of above in 25 mins):
# #   - In the tests I missed adding a major edge case of [9] becoming [1, 0]
# #   - I made a mistake in run_tests(), the line 'actual = f(expected)' should
# #     actually be 'actual = f(test)'
# #   - Additionally, the list can also be changed in place, meaning in run_test
# #     even if the line 'actual = f(expected)' is changed to actual = f(test), it 
# #     still may result in an incorrect error message. Hence it should be changed
# #     to 'actual = f(test.copy)'
# #   - Even with the above changes, plus_one() doesn't pass the tests and either
# #     way the input [9] produces [1] which is incorrect   
# #   - As such, I will rewrite plus_one(), and my new answer is below:
# # 
# # def plus_one(digits: List[int]) -> List[int]:
# #      if not digits:
# #           return digits
# #      i = len(digits) - 1
# #      while i >= 0:
# #           if digits[i] < 9:
# #                digits[i] += 1
# #                return digits
# #           else:
# #                digits[i] = 0
# #                i -= 1
# #      return [1] + digits
     


