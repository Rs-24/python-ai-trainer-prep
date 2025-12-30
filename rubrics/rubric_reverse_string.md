String Reverser Rubric:

Function:
    - reverse_string(s: str) -> str

Objective:
    - To create function reverse_string(s: str) -> str, that takes in a string
      s, and returns the reversed version of that string. If s is empty, then
      "" is returned

Inputs:
    - s, the input string to reverse

Output:
    - A string variable containing the reversed form of s

Example tests:
    - reverse_string("abc") = "cba"
    - reverse_string("123") = "321"
    - reverse_string("a b  2") = "2  b a"
    - reverse_string("") = ""
    
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
            - Optimal time complexity of O(n) via making a single pass through
              the string
            - Optimal auxiliary space complexity of O(n), where the only 
              major space taken is the reversed string. There may be 
              additional O(1) space taken up via peripheral variables
              however this is negligible
        - 1 point:
            - Either one of optimal time or space complexity, but not both, e.g. 
              either a single pass made through the string for O(n) time and many
              unnecessary variables of O(n) space, or only a single O(n) variable
              but a loop involving string concatenation leading to O(n^2) time
        - 0 points:
            - Neither optimal time nor space complexity, e.g. loop with 
              string concatenation leading to O(n^2) time complexity, and many unnecessary variables of O(n) size   
    - Readability (2 points max):
        - 2 points:
            - All variables are appropriately named
            - The program logic is generally easy to understand
        - 1 point:
            - Either program logic is not very easy to understand, or variables 
              are not appropriately named
        - 0 points:
            - Program logic is not easy to understand and variables are not 
              appropriately named
    - Correctness (3 points max):
        - 3 points:
            - No flaws in code
            - All normal tests pass
            - All edge case tests pass including:
                - empty string, e.g. ""
                - single character, e.g. "a"
                - string with spaces, e.g. "a b"
        - 2 points:
            - Any of 2 of the above points hold true 
        - 1 point:
            - Any of 1 of the above points hold true
        - 0 points:
            - None of the above points hold true
    - Tests (2 points max):
        - 2 points:
            - There are at least three normal tests
            - There are at least 3 edge case tests including:
                - empty string, e.g. ""
                - single character, e.g. "a"
                - string with spaces, e.g. "a b"
        - 1 point: 
            - Either an adequate number of normal or edge case tests, but
              not both
        - 0 points:
            - Not enough normal and edge case tests
    - Total score:
        - 8-9 points: Extremely good solution
        - 6-7 points: Good solution, may need some improvements
        - 4-5 points: Ok solution, may need significant improvements
        - 0-3 points: Bad solution, may need a complete rewrite

Advice for graders:
    - First input a few normal and edge case strings to check if the code
      generally works, then check if the code is easy to follow and the 
      variables are named appropriately, then complete the grading rubric
      above 










