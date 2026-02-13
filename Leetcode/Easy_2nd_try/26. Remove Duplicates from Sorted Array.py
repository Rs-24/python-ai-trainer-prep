




































































# # Time to write all of below including tests, why the solution works and time 
# # and space complexity: 2h 27 mins

# # I couldn't figure this one out for some reason, and I required help from
# # chatGPT to solve it

# # Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# from typing import List, Callable

# def remove_duplicates_from_sorted_array_in_place(nums: List[int]) -> int:
#     if not nums:
#         return 0
#     left = 1
#     for right in range(1, len(nums)):
#         if nums[right-1] != nums[right]:
#             nums[left] = nums[right]
#             left += 1
#     nums[left:] = ["_"] * (len(nums) - left)
#     return left

# def run_tests(f: Callable[[List[int]], int]) -> None:
#     tests = [([1, 1, 2], 2), ([], 0), ([1, 2, 3], 3), ([1, 1, 1], 1)]
#     for test, expected in tests:
#         actual = f(test)
#         assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"

# def test() -> None:
#     print("Running tests...")
#     run_tests(remove_duplicates_from_sorted_array_in_place)
#     print("All tests passed!")

# if __name__ == "__main__":
#     test()

# # Why this solution works:
# #   - if nums is empty, then 0 is automatically returned. Otherwise, a two
# #     pointer approach is used while iterating over the list and once the for 
# #     loop ends all duplicates are replaced with underscores and the number of
# #     unique elements is returned  
# #
# # Time complexity: O(len(nums))
# # Space complexity: O(len(nums))



# # Learning lessons (done after completing all of above in 2h 27 mins):
# #   - I now realise I replaced the duplicates with strings (the underscores),
# #     when the list is meant to be a list of integers. The Leetcode problem
# #     page already said that it doesn't matter what is left after all the 
# #     non-duplicates, so it would have been better to leave them as duplicates 
# #   - The tests should probably include asserts to ensure the list has also been
# #     changed correctly. Hence, run_tests() could be improved in the following 
# #     way:
# #
# # def run_tests(f: Callable[[List[int]], int]) -> None:
# #     tests = [([1, 1, 2], [1, 2], 2), ([], [], 0), ([1, 2, 3], [1, 2, 3], 3), ([1, 1, 1], [1], 1), ([0, 0, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5)]
# #     for test, expected_sublist, expected in tests:
# #         before = test.copy()
# #         actual = f(before)
# #         assert actual == expected, f"{f.__name__}({test}) = {actual}, expected {expected}"
# #         assert before[:actual] == expected_sublist, f"{f.__name__}({test}) changes {test} to {before}, but the sublist with unique numbers in {before} should be {expected_sublist}"
# #
# #