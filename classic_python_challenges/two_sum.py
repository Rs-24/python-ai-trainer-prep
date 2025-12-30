# Problem statement: to create a python program that takes in a list of 
# numbers from the user, checks to ensure it contains at least two 
# elements, and then takes in a number to find sums of, and then outputs
# the pairs in the list that sum to that number, if any

# Why this method works: the program successfully takes in a list of 
# numbers from the user, checks to ensure it contains at least two 
# elements, takes in a number to find sums of, and outputs the pairs 
# in the list that sum to that number, if any

# The calculate_two_sum() function has a time complexity of O(n) 
# where n is the number of numbers in the user's list. The function
# also has an auxiliary space complexity of O(n), as the sums 
# dictionary and seen set are used which both at their worst case 
# take up O(n) space. There are a couple of other variables used, 
# (n1 and n2), however these take up O(1) space

from typing import List, Dict

def get_list() -> List[int]:
    s = input("Please enter a list of at least two numbers:\n")
    while True:
        if s:
            nums = get_nums(s)
            if len(nums) >= 2:
                return nums
        s = input("You must enter a list of at least two numbers. Try again:\n")

def get_sum_num() -> int:
    n = input("Please enter the number to check the sums against:\n")
    while True:
        if n:
            num = get_nums(n)
            if len(num) == 1:
                return num[0]
        n = input("You must enter a single, valid number:\n")

def get_nums(s: str) -> List[int]:
    """
    Extracts a list of numbers (including negative numbers) from the string s,
    and stores them in the list nums. The only input is the string s, and the 
    only output is the list nums  
    """
    nums = []
    current_int = ""
    sign = 1
    for ch in s:
        if ch == "-":
            if current_int:
                nums.append(sign * int(current_int))
                current_int = ""
            sign = -1
        elif ch.isdecimal():
            current_int += ch
        else:
            if current_int:
                nums.append(sign * int(current_int))
                current_int = ""
            sign = 1
    if current_int:
        nums.append(sign * int(current_int))
    return nums

def calculate_two_sum(nums: List[int], num: int) -> Dict[int, int]:
    """
    Finds pairs of numbers in the list nums that sum to the int num. The only
    inputs are the list nums and the int num, and the only output is the 
    dictionary sums that contains the pairs
    """
    sums: Dict[int, int] = {}
    seen = set()
    for n1 in nums:
        n2 = num - n1
        if n2 in seen:
            if n1 not in sums and n1 not in sums.values():
                if n1 < n2:
                    sums[n1] = n2
                else:
                    sums[n2] = n1
        seen.add(n1)
    return sums

def test():
    print("Running tests...")
    assert get_nums("5-4d8b3") == [5, -4, 8, 3]
    assert get_nums("a2 4g (0) u 3_4") == [2, 4, 0, 3, 4]
    assert calculate_two_sum([1, 2, 3, 4], 5) == {1: 4, 2: 3}
    assert calculate_two_sum([-1, 2, -3, 4], -4) == {-3: -1}
    assert calculate_two_sum([1, 2, 3, 4], 8) == {}
    assert calculate_two_sum([2, 2, 2, 2], 4) == {2: 2}
    assert calculate_two_sum([-2, -2, 4, 4], 2) == {-2: 4}
    assert calculate_two_sum([], 5) == {}
    assert calculate_two_sum([5], 5) == {}
    print("All tests passed!")

def restart() -> bool:
    r = input("Would you like to restart? (y/n)\n").lower()
    while True:
        if r and r.startswith("y"):
            return True
        elif r and r.startswith("n"):
            return False
        else:
            r = input("Please enter y or n\n").lower()

def main():
    print("Welcome to the two_sum calculator!")
    while True:
        l = get_list()
        n = get_sum_num()
        sums = calculate_two_sum(l, n)
        if sums:
            print(f"The sums of {n} in {l} are:")
            for key in sums.keys():
                print(f"{key} and {sums[key]}")
        else:
            print(f"There are no sums of {n} in {l}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()