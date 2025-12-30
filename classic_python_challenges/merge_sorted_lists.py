# problem statement: to create a python program that takes two input 
# lists from the user, checks that they're both ordered, then merges them and
# outputs the sorted merged list 

# why the below method works: the program successfully takes two input lists
# (in the form of strings) from the user, checks that they contain ordered
# lists, then merges them, sorts them and then outputs the sorted merged list
# to the user. The program has a time complexity of O(n + m), where n and m
# are the number of characters used in each list respectively, because 
# get_list() is called twice, and each time it is called it calls get_nums(),
# which makes one pass through each list, so O(n + m), and check_if_ordered,
# which also makes one pass through each list, so also O(n + m). Then 
# merge_lists() is called, which merges the lists and sorts them by making
# a pass through each list, so merge_lists() is O(n + m). Hence, the overall
# time complexity is O(n + m) as the overall time grows linearly with n and m.
# It has a space complexity of O(n + m), as there are no data structures 
# stored in memory that grow more than linearly with n and m

from typing import List

def get_list(first_request: bool) -> List[int]:
    """
    Gets an input list from the user (in the form of a string), extracts the
    numbers and checks if they form an ordered list, then returns that ordered
    list.
    The only input is first_request, so the function knows whether to print
    "Please enter a sorted list:\n" or "Please enter another sorted list:\n",
    and the only output is the extracted ordered list
    """
    while True:
        if first_request:
            user_list = input("Please enter a sorted list:\n")
        else:
            user_list = input("Please enter another sorted list:\n")
        if user_list and any(ch.isdecimal() for ch in user_list): 
            nums = get_nums(user_list)
            if check_if_ordered(nums):
                break
        print("There must be an ordered list in your answer")
    return nums

def get_nums(given_list: str) -> List[int]:
    nums = []
    currentInt = ""
    sign = 1
    for ch in given_list:
        if ch.isdecimal():
            currentInt += ch
        elif ch == "-":
            if currentInt != "":
                nums.append(sign * int(currentInt))
                currentInt = ""
            sign = -1
        else:
            if currentInt != "":
                nums.append(sign * int(currentInt))
                currentInt = ""
            sign = 1
    if currentInt != "":
        nums.append(sign * int(currentInt))
    return nums

def check_if_ordered(given_list: List[int]) -> bool:
    if not given_list:
        return False
    last_item = given_list[0]
    for item in given_list[1:]:
        if item < last_item:
            return False
        last_item = item
    return True

def restart() -> bool:
    while True:
        r = input("Would you like to restart? (y/n)\n").lower()
        if r:
            if r.startswith("y"):
                return True
            if r.startswith("n"):
                return False
        print("Please enter a valid answer")
        
def merge_lists(a: List[int], b: List[int]) -> List[int]:
    i, j = 0, 0
    l = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
    l += a[i:]
    l += b[j:]
    return l

def test():
    print("Running tests")
    assert get_nums("fh89f8r7-4") == [89, 8, 7, -4]
    assert not check_if_ordered([1, 9, -4])
    assert check_if_ordered([-1, 0, 9])
    assert merge_lists([-1, 5, 8], [2, 6, 10]) == [-1, 2, 5, 6, 8, 10]
    print("All tests passed!")

def main():
    while True:
        print("Welcome to the list merger!")
        list1 = get_list(1)
        list2 = get_list(0)
        print(f"{list1} and {list2} merged is: {merge_lists(list1, list2)}")
        if not restart():
            break

if __name__ == "__main__":
    test()
    main()