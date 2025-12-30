# problem statement: to create a python program that takes a string with at
# least two numbers from the user, extracts the numbers and outputs the second
# largest number

# why this method works: the program successfully takes an input string in from
# the user, checks if it contains at least two numbers, extracts the numbers in 
# the form of a list, find the second largest number, and outputs it to the
# user. Assuming n is the number of characters in the string the user enters, 
# and k is the number of numbers extracted from that string, get_nums() calls 
# extract_nums(), which makes a full pass through the string, so O(n). 
# get_nums() also creates a set of the extracted numbers, so O(k).
# Then get_second_largest_number() is called, which creates a set of the 
# extracted numbers again, so O(k). It then sorts the remaining data, so
# O(d log d) where d is the number of remaining elements after creating a set
# of the extracted numbers, where d <= k. Hence the overall time complexity is 
# O(n + k + d log d). The space complexity is O(n), as no variables stored in
# memory vary more than linearly with n

from typing import List

def get_nums() -> List[int]:
    while True:
        s = input("Please enter a string with at least two numbers:\n")
        if s:
            nums = extract_nums(s)
            if len(set(nums)) >= 2:
                return nums
        print("There must be at least two distict numbers in your answer")

def extract_nums(given_string: str) -> List[int]:
    if not given_string:
        return []
    current_int = ""
    sign = 1
    nums = []
    for ch in given_string:
        if ch.isdecimal():
            current_int += ch
        elif ch == "-":
            if current_int != "":
                nums.append(sign * int(current_int))
                current_int = ""
            sign = -1
        else:
            if current_int != "":
                nums.append(sign * int(current_int))
                current_int = ""
            sign = 1
    if current_int != "":
        nums.append(sign * int(current_int))
    return nums

def get_second_largest_number(given_nums: List[int]) -> int:
    distinct_nums = set(given_nums)
    if len(distinct_nums) >= 2:
        return sorted(distinct_nums)[-2]
    else:
        raise ValueError("There should be at least two distinct numbers")
        
def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n)\n").lower()
        if r:
            if r.startswith("y"):
                return True
            elif r.startswith("n"):
                return False
        print("Please enter a valid answer")

def test():
    print("Running tests...")
    assert extract_nums("fg4 37 -r7 -4fre 7-2") == [4, 37, 7, -4, 7, -2]
    assert get_second_largest_number([2, 3, 4, -3, 9]) == 4
    assert get_second_largest_number([1, 1, 2, 2, 3, 3]) == 2
    assert get_second_largest_number([-10, -5, -3, -3]) == -5
    try:
        get_second_largest_number([5, 5])
        assert False, "There should be at least two distinct numbers"
    except ValueError:
        pass
    print("All tests passed")

def main():
    while True:
        print("Welcome to the second largest number finder!")
        nums = get_nums()
        print(f"The second largest number in {nums} is {get_second_largest_number(nums)}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()