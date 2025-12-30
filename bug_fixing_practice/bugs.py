from typing import List, Dict

# Note: at the end all intentional bugs were reverted back to the correct
# versions, and all tests passed

def merge_lists(a: List[int], b: List[int]) -> List[int]:
    i, j = 0, 0
    l = []
    while i <= len(a) and j <= len(b): # while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
    l += a[i:]
    l += b[j:]
    return l

def validate_balanced_parentheses(s: str) -> bool:
    pairs = {")": "(", "}": "{", "]": "["}
    order = []
    for ch in s:
            if ch in "{[": # if ch in "({[":
                order.append(ch)
            elif ch in ")}": # elif ch in ")}]":
                if not order or order[-1] != pairs[ch]:
                    return False
                order.pop()
    return not order

def binary_search(nums: List[int], n: int) -> int:
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
    return 1 # return -1

def calculate_two_sum(nums: List[int], num: int) -> Dict[int, int]:
    sums: Dict[int, int] = {}
    seen = set()
    for n1 in nums:
        n2 = num - n1
        if n2 in seen:
            if n1 not in sums and n1 not in sums.values():
                if n1 > n2: # if n1 < n2:
                    sums[n1] = n2
                else:
                    sums[n1] = n2 # sums[n2] = n1
        seen.add(n1)
    return sums

def compress_string(s: str) -> str:
    if not s:
        return ""
    compressed = []
    prev_ch = s[1] # prev_ch = s[0]
    num_instances = 0
    for ch in s:
        if ch == prev_ch:
            num_instances += 1
        else:
            compressed.append(prev_ch + str(num_instances))
            num_instances = 1 
        prev_ch = ch
    compressed.append(prev_ch + str(num_instances))
    return "".join(compressed)

def assert_equal(function, expected, message) -> None:
    try:
        actual = function()
    except Exception as e:
        print(f"Fail: {message}, raised {type(e).__name__}, {e}")
        return
    if actual == expected:
        print(f"Pass: {message}")
    else:
        print(f"Fail: {message}, expected: {expected}, got: {actual}")

def test_merge_sorted_lists():
    print("____merge sorted lists____")
    assert_equal(lambda: merge_lists([-1, 5, 8], [2, 6, 10]), [-1, 2, 5, 6, 8, 10], "Basic")
    # above got error: "Fail: Basic, raised IndexError, list index out of range"
    # this is because the line: 'while i < len(a) and j < len(b):' was changed to 'while i <= len(a) and j <= len(b):' 
    # so that whenever a[i] or b[j] was called the index would be out of the range as indexes alway start at 0 and 
    # end at the length - 1
    print("-" * 10)

def test_validate_balanced_parentheses():
    print("____balanced parentheses____")
    assert_equal(lambda: validate_balanced_parentheses(""), True, "Empty")
    assert_equal(lambda: validate_balanced_parentheses("(a){b}c[]"), True, "letters and brackets")
    # above failed: "Fail: letters and brackets, expected: True, got: False". This is because the line 
    # 'if ch in "({[":' was changed to 'if ch in "{[":', therefore some open and close brackets were
    # unaccounted for, therefere meaning a faulty determination on whether the parentheses were properly
    # balanced
    assert_equal(lambda: validate_balanced_parentheses("({[]})"), True, "Nested parentheses")
    # Above got fail for same reason as first fail
    assert_equal(lambda: validate_balanced_parentheses("({"), False, "Only open parentheses")
    assert_equal(lambda: validate_balanced_parentheses("([)]"), False, "Wrong order")
    assert_equal(lambda: validate_balanced_parentheses("}]])"), False, "Only close brackets")
    assert_equal(lambda: validate_balanced_parentheses("(((())))"), True, "Nested balanced parentheses")
    # Above got fail for same reason as first fail
    assert_equal(lambda: validate_balanced_parentheses(")}{("), False, "Inside out")
    print("-" * 10)

def test_binary_search():
    print("____binary search____")
    assert_equal(lambda: binary_search([1, 2, 3, 4], 3), 2, "Basic")
    assert_equal(lambda: binary_search([-3, 4, 8, 10], 5), -1, "Not in list")
    # above failed: 'Fail: Not in list, expected: -1, got: 1', this is because the line 'return -1' was 
    # changed to 'return 1'. When the number is not in the list, the function is supposed to return -1, 
    # but due to the changed line returned 1, therefore causing the failed test
    assert_equal(lambda: binary_search([1], 1), 0, "Single element")
    assert_equal(lambda: binary_search([1], 2), -1, "Single element not in list")
    # above failed: 'Fail: Single element not in list, expected: -1, got: 1;', this failed for the same 
    # reason as the first failure
    assert_equal(lambda: binary_search([1, 2, 3, 4], 1), 0, "Basic")
    assert_equal(lambda: binary_search([1, 2, 3, 4], 4), 3, "Basic")
    assert_equal(lambda: binary_search([-5, -2, 0, 3, 7], -5), 0, "Longer list")
    assert_equal(lambda: binary_search([-5, -2, 0, 3, 7], 7), 4, "Longer list")
    print("-" * 10)

def test_two_sum():
    print("____two sum____")
    assert_equal(lambda: calculate_two_sum([1, 2, 3, 4], 5), {1: 4, 2: 3}, "Basic")
    # above failed: 'Fail: Basic, expected: {1: 4, 2: 3}, got: {3: 2, 4: 1}', this is because the code block
    # 'if n1 < n2: sums[n1] = n2 else: sums[n2] = n1' was changed to: 'if n1 > n2: sums[n1] = n2 else: sums[n1] = n2
    # the initial code block ensured that pairs in the consisted had the smaller number as the key and the larger 
    # number as the value, however this code change gives the opposite, hence causing the error.  
    assert_equal(lambda: calculate_two_sum([-1, 2, -3, 4], -4), {-3: -1}, "Basic")
    assert_equal(lambda: calculate_two_sum([1, 2, 3, 4], 8), {}, "No sum")
    assert_equal(lambda: calculate_two_sum([2, 2, 2, 2], 4), {2: 2}, "Homogeneous list")
    assert_equal(lambda: calculate_two_sum([-2, -2, 4, 4], 2), {-2: 4}, "Basic, with repeated items in list")
    # above failed: 'Fail: Basic, with repeated items in list, expected: {-2: 4}, got: {4: -2}'. This failed for the
    # same reason as the first failure
    assert_equal(lambda: calculate_two_sum([], 5), {}, "Empty list")
    assert_equal(lambda: calculate_two_sum([5], 5), {}, "Single item in list")
    print("-" * 10)

def test_compress_string():
    print("____compress string____")
    assert_equal(lambda: compress_string("aaabb"), "a3b2", "Basic")
    assert_equal(lambda: compress_string("a  b"), "a1 2b1", "Basic, with spaces")
    # above failed: 'Fail: Basic, with spaces, expected: a1 2b1, got:  0a1 2b1', this is because the line 'prev_ch = s[0]'
    # was changed to 'prev_ch = s[1]', which meant the first character of the compressed string would be the second
    # character in the initial string, in this case the space " ". Additionally this causes num_instances to remain 
    # unchanged at 0 for the first character, which causes the compressed string to start with " 0". After this the program
    # corrects itself and the remainder of the compressed string is the same as the expected compressed string. However, the 
    # beginning is still ' 0' which caused the failed test
    assert_equal(lambda: compress_string(""), "", "Empty string")
    assert_equal(lambda: compress_string("a"), "a1", "Single character")
    # above failed: 'Fail: Single character, raised IndexError, string index out of range'
    # this is because there is only one element, and hence only one index of 0, however the line 'prev_ch = s[0]' was
    # changed to 'prev_ch = s[1]', which meant the index was out of the range, and hence caused the fail/error
    assert_equal(lambda: compress_string("aaaa"), "a4", "Same character multiple times")
    assert_equal(lambda: compress_string("abcd"), "a1b1c1d1", "Basic, one letter each")
    # above failed: 'Fail: Basic, one letter each, expected: a1b1c1d1, got: b0a1b1c1d1', this is because of the same reason as
    # the first fail.
    assert_equal(lambda: compress_string("AAaa"), "A2a2", "Upper and lower case")
    assert_equal(lambda: compress_string("1112221"), "132311", "Only numbers")
    print("-" * 10)

def main():
    test_merge_sorted_lists()
    test_validate_balanced_parentheses()
    test_binary_search()
    test_two_sum()
    test_compress_string()

if __name__ == "__main__":
    main()






