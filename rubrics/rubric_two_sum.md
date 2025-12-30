Two sum rubric:

Function:
    - two_sum(nums: List[int], target: int) -> Dict[int, int]

Objective:
    - To create a function 
      two_sum(nums: List[int], target: int) -> Dict[int, int], that takes in
      a List of numbers from the user and a target integer, and returns a 
      dictionary containing the unique pairs of numbers in nums that sum to
      target (so no duplicate pairs). Each pair in the dictionary has the 
      smaller value as the key, and the larger value as the value

Inputs:
    - nums: the list of numbers
    - target: the number which the pairs should sum to

Outputs:
    - A dictionary containing the unique pairs in nums that sum to target
      (so no duplicate pairs). Each pair in the dictionary has the 
      smaller value as the key, and the larger value as the value

Example tests:
    - two_sum([1, 2, 3], 3) = {1: 2}
    - two_sum([], 3) = {}
    - two_sum([1, 1, 1, 1], 2) = {1: 1}

Grading rubric:
    - Complexity:
        - Does the program have an optimal time complexity?
        - Does the program have an optimal auxiliary space complexity?
    - Readability:
        - Is the program logic easy to understand?
        - Are all the variables appropriately named?
    - Correctness:
        - Are there any flaws in the code?
        - Do all inputs give the correct output including edge cases
    - Tests:
        - Are there an adequate number of normal tests
        - Are there an adequate number of edge case tests

Grading scale:
    - Complexity (2 points max):
        - 2 points:
            - Optimal time complexity of O(n) from iterating through the list
            - Optimal auxiliary space complexity of O(n), consisting of the 
              dictionary of pairs. There may be additional variables taking up
              O(1) space
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Readability (2 points max):
        - 2 points:
            - Program logic easy to understand
            - All variables appropriately named
        - 1 points:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Correctness (3 points max):
        - 3 points:
            - No major flaws in program logic
            - Program correctly identifies all unique pairs that sum to 
              target (so no duplicates)
            - Correctly handles all edge case inputs including:
                - Empty nums, [], with any target, e.g. 0, 5, 9, etc
                - Multiple duplicates, e.g. nums = [1, 1, 1, 1], target = 2
                - Negative numbers, e.g. nums = [-1, 3, 4], target = 2
                - Single element, e.g. nums = [1], with any target, e.g. 1, 2, 5
        - 2 points:
            - Only two of the above points hold true
        - 1 point:
            - Only one of the above points hold true
        - 0 points:
            - None of the above points hold true
    - Tests (2 points max):
        - 2 points:
            - There are at least 3 normal tests
            - There are at least 4 edge case tests including:
                - Empty nums, [], with any target, e.g. 0, 5, 9, etc
                - Multiple duplicates, e.g. nums = [1, 1, 1, 1], target = 2
                - Negative numbers, e.g. nums = [-1, 3, 4], target = 2
                - Single element, e.g. nums = [1], with any target, e.g. 1, 2, 5
        - 1 point:
            - Only one of the above points hold true
        - 0 points:
            - None of the above points hold true
    - Total score:
        - 8-9 points: Very good solution, may require minor improving
        - 6-7 points: Good solution, requires some improving
        - 4-5 points: Ok solution, needs significant improving
        - 0-3 points: Not a good solution, may need completely rewriting

Advice for graders:
    - First input some normal and edge case inputs to see if the program can
      handle them
    - Then see if the program logic is easy to understand and if the variables 
      are all named correctly
    - Then check to see if it has optimal time and auxiliary space complexity
    - Then grade the code according to the grading scale above
                





