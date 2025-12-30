def moving_average(values, window_size: int):
    """
    Compute a simple moving average.
    """
    if window_size <= 0:
        raise ValueError("window_size must be > 0")
    result = []
    for i in range(len(values) - window_size + 1):
        window = values[i:i+window_size]
        result.append(sum(window) / len(window))
    return result

Note: the above code was written by chatGPT

How the code works:
    - The code takes in a list of values and a window size, and computes the
      moving average
    - First, it checks if window size is <= 0, and if it is, raises a
      ValueError
    - Then it creates an empty list called 'result', and iterates through from
      to the furthest point possible allowing for the window length
    - In each iteration, the sum of the window of values is calculated and
      divided by the length of the window. This value is then appended to results
    - Once the loop ends, result is returned

Good aspects of the code:
    - Program logic is easy to understand
    - All variables are appropriately named
    - Window_size is first checked to ensure it isn't <= 0

Risky aspects of the code:
    - If window_size > len(values), then the loop never runs, and [] is
      returned
    - As there is no type hint for values, if it isn't a list of integers then
      the program would experience an error   

Improvements:
    - If it is expected that [] is returned if window_size > len(values), 
      then it would be advised to mention this in the docstring. If this 
      isn't the expected behaviour, then the program could either raise a ValueError if window_size > len(values), or only return 
      sum(values) / len(values). In either of these cases, it would be best
      to document this in the docstring  
    - A type hint of list[int] could be given to the 'values' parameter
    - The docstring could be more descripitive and mention that window_size is 
      checked to see if it <= 0, and if so it raises a ValueError




