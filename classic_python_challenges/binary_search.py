# Problem statement: to create a python program that takes in a list from the
# user, checks if it sorted, then takes in a number to find in that list from
# the user, and uses a binary search to find the index of that number. It then 
# outputs this index, or states that the number is not in the list if the list
# does not contain the number

# Why this method works: the program successfully takes in a list from the
# user, checks if it is sorted, then takes in a number to find in that list,
# then uses a binary search to find the index of that number and outputs 
# it or states that the number is not in the list if so. 

# The binary_search() function has a time complexity of O(log n), where n is
# the number of numbers in the list. It has an auxiliary space complexity of
# O(1), as only a few variables are stored in memory.

from typing import List 

def get_list() -> List[int]:
    while True:
        s = input("Please enter a sorted list:\n")
        if s:
            nums = get_nums(s)
            if nums and check_sorted(nums):
                return nums
        print("Please enter a valid answer")

def get_num_to_find() -> int:
    while True:
        n = input("Please enter the number you would like to find:\n")
        if n:
            num = get_nums(n)
            if len(num) == 1:
                return num[0]
        print("Please enter a valid answer")

def check_sorted(nums: List[int]) -> bool:
    """
    Checks if the input list nums is sorted by making a full pass through the
    list. The only input is the input list nums, and the only output is a 
    boolean True/False depending on if the list is sorted or not, and False
    if the list is empty
    """
    if not nums:
        return False
    previous_num = nums[0]
    for num in nums[1:]:
        if num < previous_num:
            return False
        previous_num = num
    return True

def get_nums(s: str)-> List[int]:
    """
    Extracts a list of numbers from the input string s including negative
    numbers. The only input is the input string s and the only output is
    the list of integers  
    """
    nums: List[int] = []
    current_int = ""
    sign = 1
    for ch in s:
        if ch.isdecimal():
            current_int += ch
        elif ch == "-":
            if current_int:
                nums.append(sign * int(current_int))
                current_int = ""
            sign = -1
        else:
            if current_int:
                nums.append(sign * int(current_int))
                current_int = ""
            sign = 1
    if current_int:
        nums.append(sign * int(current_int))
    return nums

def binary_search(nums: List[int], n: int) -> int:
    """
    Performs a binary search on the list nums, searching for the number n. The
    nums list must not be empty as a precondition. The only inputs are the list
    of numbers, nums, and the number to find, n, and the only output is the 
    index at which n is at, or -1 if n is not in the list 
    """
    if not nums:
        return -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > n:
            right = mid - 1
        elif nums[mid] < n:
            left = mid + 1
        else:
            return mid
    return -1

def test():
    print("Running tests...")
    assert check_sorted([2, 3, 5, 1]) == False
    assert check_sorted([2, 7, 0]) == False
    assert check_sorted([-3, 2, 5, 10]) == True
    assert get_nums("2 3 4 5") == [2, 3, 4, 5]
    assert get_nums("2-9abc-3b78") == [2, -9, -3, 78]
    assert binary_search([1, 2, 3, 4], 3) == 2
    assert binary_search([-3, 4, 8, 10], 5) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1
    assert binary_search([1, 2, 3, 4], 1) == 0
    assert binary_search([1, 2, 3, 4], 4) == 3
    assert binary_search([-5, -2, 0, 3, 7], -5) == 0
    assert binary_search([-5, -2, 0, 3, 7], 7) == 4
    print("All tests passed!")

def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n)\n").lower()
        if r and r.startswith("y"):
            return True
        elif r and r.startswith("n"):
            return False
        print("Please enter a valid answer")

def main():
    print("Welcome to the Binary Search Algorithm!")
    while True:
        l = get_list()
        n = get_num_to_find()
        b = binary_search(l, n)
        if b < 0:
            print(f"{n} is not in {l}")
        else:
            print(f"{n} is at index {b} in {l}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()