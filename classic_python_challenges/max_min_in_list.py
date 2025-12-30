# problem statement: to create a python program that takes 
# a string containing integers from the user, and outputs the largest and smallest 
# integers in the string

# why the below method works: the program successfully takes an input string 
# from the user and checks to confirm that it contains integers, 
# and then strips away the other characters, and iterates over the remaining
# characters to determine the largest and smallest values. The program has a 
# time complexity of O(n) (or specifically O(n+k)), as convert_to_ints() goes 
# through each character in the string once, so O(n), and both find_max() and 
# find_min() go through each of the remaining characters once, so O(k) for each 
# where k is the number of remaining characters. So the overall time complexity 
# is O(n + k), or O(n) for short. It has a space complexity of O(k), where k 
# is the number of integers extracted, as once the non-integer characters
# are removed, the remaining string is stored in memory 

def get_string():
    while True:
        string = input("Please enter a string with numbers:\n")
        if string and any(ch.isdecimal() for ch in string): 
            return string

def restart():
    while True:
        restartAnswer = input("Would you like to start again?\n")
        if restartAnswer.lower().startswith("y"):
            return True
        elif restartAnswer.lower().startswith("n"):
            return False
        else: 
            print("Please enter a valid answer")

def convert_to_ints(given_string):
    nums = []
    sign = 1
    currentInt = ""
    for ch in given_string:
        if ch == "-":
            if currentInt == "":
                sign = -1
            else:
                nums.append(sign * int(currentInt))
                sign = -1
                currentInt = ""
        elif ch.isdecimal():
            currentInt += ch
        else:
            if currentInt != "":
                nums.append(sign * int(currentInt))
                currentInt = ""
            sign = 1
    if currentInt != "":
        nums.append(sign * int(currentInt))
    return nums

def find_min_max(given_nums):
    if not given_nums:
        return None
    smallest = largest = given_nums[0]
    for num in given_nums[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return smallest, largest

def main():
    while True:
        print("Welcome to the max/min finder!")
        string = get_string()
        string_ints = convert_to_ints(string)
        if not string_ints:
            print("No valid integers found")
            continue
        min_val, max_val = find_min_max(string_ints)
        print(f"Smallest number: {min_val}")
        print(f"Largest number: {max_val}")
        
        if not restart():
            break

if __name__ == "__main__":
    main()

