class Timer:
    """
    Simple timing context manager.
    """
    def __init__(self):
        self.start = None
        self.end = None
        self.elapsed = None

    def __enter__(self):
        import time
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc, tb):
        import time
        self.end = time.time()
        self.elapsed = self.end - self.start

Note: the above code was written by chatGPT

How the code works:
    - The code creates a context manager which could be used in the 
      following way:
        - with Timer() as t:
            do_something()
          print(t.elapsed) # prints time taken to run do_something
    - The initialization function __init__ initializes three attributes:
        - start, which is the start time
        - end, which is the end time
        - elapsed, which is the elapsed time, i.e. end - start
    - The __enter__ function starts the timer by setting start to the
      current time. The function also returns self, so the line
      'with Timer() as t:' runs and so that t.elapsed can be accessed
      after the with statement ends
    - The __exit__ function stops the timer by setting end to the current
      time, and setting elapsed to end - start

Good aspects of the code:
    - Program logic easy to understand
    - All variables appropriately named
    - Docstring succintly states what the program does

Risky aspects of the code:
    - No significant risky aspects of the code

Improvements:
    - Have import time outside the class at the start of the program instead
      of in the __enter__ and __exit__ functions to avoid repetition and make
      the program look neater, and note in the docstring that import time is required outside the class at the start of the program
    - Use time.perf_counter() instead of time.time() for a more accurate
      result
    





