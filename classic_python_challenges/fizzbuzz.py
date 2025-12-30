# problem statement: to create a python program that uses a for loop 
# from 1 to a given number of integers (in this case 100), and prints "Fizz"
# if the number is divisible by 3, "Buzz" if the number is divisible by 5, 
# "FizzBuzz" if the number is divisible by both 5 and 3, and the number itself
# if none of these conditions hold

# why the below method works: the program successfully loops from 1 to a given
# number of integers (in this case 100), and appends "Fizz" if the number is 
# divisible by 3, "Buzz" if the number is divisible by 5, "FizzBuzz" if the
# number is divisible by both 5 and 3, and string form of the number itself
# if none of these conditions hold to a list in the fizz_buzz function. The 
# program has a time complexity of O(n), where n is the number of integers 
# the program iterates over, in this case 100. This is because a constant 
# amount of work is done for each integer so the overall time grows 
# linearly with n. It has a space complexity of O(n), as there is only one 
# data structure stored in memory that grows linearly with n, which is the 
# result list in the fizz_buzz function 

from typing import List

def fizz_buzz(given_num_ints: int) -> List[str]:
    """
    Returns the fizzbuzz sequence in the form of a list from 1 to given_num_ints
    (inclusive). The fizzbuzz sequence is "Fizz" if the number is divisible by 3,
    "Buzz" if the number is divisible by 5, "FizzBuzz" if the number is divisible
    by both 5 and 3, and the string form of the number itself if none of these
    conditions hold.
    The only input is given_num_ints, and the output is the list (named result)
    which contains either "Fizz", "Buzz", "FizzBuzz", or the current number in
    the loop
    Raises:
        ValueError: If given_num_ints < 1
    """
    if given_num_ints < 1:
        raise ValueError("given_num_ints must be >= 1")
    result = []
    for i in range(1, given_num_ints + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def test_fizz_buzz():
    assert fizz_buzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert fizz_buzz(1) == ["1"]
    assert fizz_buzz(15)[-1] == "FizzBuzz"

def main():
    print("Welcome to FizzBuzz!")
    for item in fizz_buzz(100):
        print(item)


if __name__ == "__main__":
    test_fizz_buzz()
    main()