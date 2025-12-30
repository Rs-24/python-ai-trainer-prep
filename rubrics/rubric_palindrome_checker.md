Palindrome Checker Rubric:

Function:
    - palindrome_checker(s: str) -> bool

Objective:
    - To create a function palindrome_checker(s: str) -> bool, which determines
      whether the string s is a palindrome, excluding spaces (so only considering non-space characters, case-insensitive). If s is empty, returns True 

Inputs:
    - s, the input string

Output:
    - A single boolean True/False, depending on whether the input string s is a 
      palindrome or not, excluding spaces and only considering non-space characters, case-insensitive

Example tests:
    - palindrome_checker("abc") = False
    - palindrome_checker("") = True
    - palindrome_checker(" ") = True
    - palindrome_checker("racecar") = True
    - palindrome_checker("taco cat") = True
    - palindrome_checker("a b") = False
    - palindrome_checker("a") = True

Grading rubric:
    - Complexity: 
        - Does it have an optimal time complexity?
        - Does it have an optimal auxiliary space complexity?        
    - Readability: 
        - Is the code easy to understand?
        - Are the variables appropriately named?
    - Correctness:
        - Are there any flaws in the code?
        - Do all inputs give correct outputs including edge cases?
    - Tests:
        - Are there an adequate number of normal tests?
        - Are there an adequate number of edge case tests?

Grading scale:
    - Complexity (2 points max):
        - 2 points: 
            - Optimal time complexity of O(n), via iterating through each 
              character of the string
            - Optimal auxiliary space complexity of O(1) whereby only the
              specific characters from the string are compared per iteration.There may be additional O(1) variables which are fine to have
        - 1 point:
            - Either optimal time complexity of O(n), or optimal space complexity
              of O(1), but not both. E.g. time complexity could be worse if string
              concatenation is used while iterating over the string, leading to 
              O(n^2) time, or space complexity could be worse if a reversed string of O(n) space is stored in memory
        - 0 points:
            - Neither optimal time nor space complexity, e.g. string
              concatenation is used while iterating over the string, leading to 
              O(n^2) time, and the reversed string of O(n) space is stored in memory
    - Readability (2 points max):
        - 2 points:
            - All variables appropriately named
            - Program logic is easy to understand
        - 1 point:
            - Either one of the above points hold, but not both
        - 0 points:
            - None of the above points hold
    - Correctness (3 points max):
        - 3 points:
            - No major flaws in program logic
            - Correctly identifies a palindrome and non-palindrome for all
              normal inputs 
            - Correctly handles all edge case inputs including:
                - Empty string, e.g. ""
                - Single space, e.g. " "
                - Letters with space, e.g. "a b"
                - Single character, e.g. "a"
        - 2 points:
            - Only two of the above points hold
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Tests (2 points max):
        - 2 points:
            - There are at least 3 normal tests
            - There are at least 4 edge case tests including:
                - Empty string, e.g. ""
                - Single space, e.g. " "
                - Letters with space, e.g. "a b"
                - Single character, e.g. "a"
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Total score:
        - 8-9 points: Very good solution, maybe only minor improvements needed
        - 6-7 points: Good solution, some improvements needed
        - 4-5 points: Ok solution, may need significant improvements
        - 0-3 points: Not a good solution, may need completely rewriting

Advice for graders:
    - First input a few normal and edge case tests to see if the program works
    - Then check to see if the code logic is easy to understand and if the
      variables are named appropriately. 
    - Then see if the time and auxiliary space complexity are optimal
    - Then complete the grading scale above


