from typing import List, Callable

def move_zeroes_simple(nums: List[int]) -> None:
    """
    Moves all zeroes in nums to end, if any. Changes the list in place, and 
    hence doesn't return anything
    """
    new_nums: List[int] = [num for num in nums if num != 0]
    num_zeroes = len(nums) - len(new_nums)
    new_nums.extend([0] * num_zeroes)
    nums[:] = new_nums

def move_zeroes_in_place(nums: List[int]) -> None: 
    """ 
    Moves all zeroes in nums to end, if any. Changes the list in place,
    and hence doesn't return anything 
    """ 
    insert_pos = 0
    for i, num in enumerate(nums): 
        if num != 0: 
            if i != insert_pos:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1

def run_test(f: Callable[[List[int]], None]) -> None:
    tests = [([1, 2, 3], [1, 2, 3]), ([0, -1, 0, -2], [-1, -2, 0, 0]), ([3, 0, 3, 0, 3], [3, 3, 3, 0, 0]), ([4, 5, 6, 7], [4, 5, 6, 7]), ([], []), ([0], [0]), ([1], [1]), ([0, 0, 0], [0, 0, 0]), ([0, 1, 2], [1, 2, 0]), ([0, 1, 0, 2], [1, 2, 0, 0])]
    for original, expected in tests:
        before = original.copy()
        actual = original.copy()
        f(actual)
        assert actual == expected, f"{f.__name__}({before}) changed it to {actual}, expected {expected}"
    
def test():
    print("Running tests...")
    run_test(move_zeroes_simple)
    run_test(move_zeroes_in_place)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# move_zeroes_simple() review:
# Correctness:
#   - Works for all edge cases, e.g. empty list, single zero element, single non-zero element, all zeroes, no zeroes, etc
#
# Complexity:
#   - Time: O(n), where n = len(nums)
#   - Space: O(n)
#
# Readability:
#   - Very easy to understand how the algorithm works, as it the function is very explicit
#
# Use case:
#   - For when teaching/understanding the algorithm are prioritised over space complexity 
#
# move_zeroes_in_place()
# Correctness:
#   - Works for all edge cases, e.g. empty list, single zero element, single non-zero element, all zeroes, no zeroes, etc
#
# Complexity:
#   - Time: O(n), where n = len(nums)
#   - Space: O(1)
#
# Readability:
#   - Slightly more difficult to understand as the function modifies the list as iterates through it
#
# Use case:
#   - For when space complexity is prioritised over teaching/understanding the algorithm
#
# Verdict:
#   - Both have the same time complexity of O(n), however move_zeroes_in_place()
#     has a space complexity of O(1) compared to move_zeroes_simple()'s O(n)
#   - Hence I would advise using move_zeroes_in_place() for production due to 
#     its superior space complexity, and move_zeroes_simple() for teaching and 
#     understanding the algorithm