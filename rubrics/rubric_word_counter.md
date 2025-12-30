Word counter rubric:

Function:
    - word_counter(s: str) -> Dict[str, int]

Objective:
    - To create a function word_counter(s: str) -> Dict[str, int], which takes
      in an input string s, and outputs a dictionary where each key is a word
      and each value is the corresponding frequency of each word in the 
      sentence. If s is empty, e.g. "", returns {}

Inputs:
    - s, the input string

Outputs:
    - A dictionary containing each word and its corresponding frequency

Example tests:
    - word_counter("a b c") = {"a": 1, "b": 1, "c": 1}
    - word_counter("") = {}
    - word_counter("Hi there there") = {"Hi": 1, "there": 2}

Grading rubric:
    - Complexity:
        - Does the program have an optimal time complexity?
        - Does the program have an optimal auxiliary space complexity?
    - Readability:
        - Is the program logic easy to understand
        - Are all the variables named appropriately?
    - Correctness:
        - Are there any major flaws in the code?
        - Do all inputs produce the correct output including edge cases?
    - Tests:
        - Are there an adequate number of normal tests
        - Are there an adequate number of edge case tests

Grading scale:
    - Complexity (2 points max):
        - 2 points:
            - Optimal time complexity of O(n) via making one pass through the list
            - Optimal auxiliary space complexity of O(n), mainly from the returned
              dictionary variable. There may be additional O(1) variables which
              are fine
        - 1 point:
            - Either one of the above points hold, but not both
        - 0 points:
            - Neither of the above points hold true
    - Readability (2 points max):
        - 2 points:
            - Program logic is easy to understand
            - All variables are appropriately named
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold true
    - Correctness (3 points max):
        - 3 points:
            - No major flaws in program logic
            - Function correctly identifies each unique word and its frequency
              (so no duplicate words)
            - Function can handle all edge cases including:
                - Single letters, e.g. "a b c" 
                - empty string, e.g. ""
                - Single letter, e.g. "a"
                - Single word, e.g. "Hi"
                - Single space, e.g. " "
        - 2 points:
            - Only two of the above points hold
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Tests (2 points max):
        - 2 points:
            - At least 3 normal tests
            - At least 5 edge case tests including:
                - Single letters, e.g. "a b c" 
                - empty string, e.g. ""
                - Single letter, e.g. "a"
                - Single word, e.g. "Hi"
                - Single space, e.g. " "
        - 1 point:
            - Only one of the above points hold
        - 0 points:
            - None of the above points hold
    - Total score:
        - 8-9 points:
            - Very good solution, may need minor improvements
        - 6-7 points:
            - Good solution, may need some improvements
        - 4-5 points:
            - Ok solution, may need significant improvements
        - 0-3 points:
            - Not a good solution, may need completely rewriting

Advice for graders:
    - First apply some normal and edge case tests to see if the function
      produces the correct output
    - Then check if the program logic is easy to understand and if all the
      variables are named correctly
    - Then check if the program has an optimal time and space complexity
    - Then grade the function according to the grading scale 
      above

 
                 


        
    
   