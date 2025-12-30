def chunk_list(items, size: int):
    """
    Yield chunks of the list with given size.
    """
    if size <= 0:
        return []
    for i in range(0, len(items), size):
        yield items[i:i+size]

Note: the above code was written by chatGPT

How the code works:
    - The code takes in a variable called 'items' and an integer called 'size',
      and splits 'items' into chunks of size 'size', and yields each chunk
    - To do this, the code first checks if size is <= 0, and if so, returns
      an empty generator (not an empty list as the function uses yield instead
      of return)
    - It then iterates over 'items' in steps of 'size', and yields each chunk
      from 'items'

Good aspects of the code:
    - Program logic is easy to understand
    - All variables appropriately named
    - Correctly handles 'size' being <= 0 without errors
    - Uses yield instead of return which is useful if 
      len(items) >> size

Risky aspects of the code:
    - If 'items' does not support slicing or len(), then then an error could
      occur and the program may not return anything
    - The chunks may not all be the same size, e.g. len(items) = 10, size = 3,
      the chunks will be of sizes 3, 3, 3, 1

Improvements:
    - Add a type hint for 'items' that support slicing and len(), 
      e.g. items: list[int] 
    - The docstring could also state that if size <= 0, then an empty generator
      is returned, and that the program yields each chunk instead of returning 
      them all. This way there can be no confusion over what the program does
      and returns
    - Also mention in the docstring that if len(items) is not divisible by 
      'size', then the chunks may not all be the same size.








