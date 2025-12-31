from classic_python_challenges import reverse_string
from classic_python_challenges import palindrome_checker
from classic_python_challenges import max_min_in_list
from classic_python_challenges import duplicate_remover
from classic_python_challenges import fizzbuzz
from classic_python_challenges import sum_of_digits_of_number
from classic_python_challenges import merge_sorted_lists
from classic_python_challenges import second_largest_number
from classic_python_challenges import rotate_string
from classic_python_challenges import count_vowels
from classic_python_challenges import check_anagram
from classic_python_challenges import validate_balanced_parentheses
from classic_python_challenges import binary_search
from classic_python_challenges import two_sum
from classic_python_challenges import compress_string

def assert_equal(actual, expected, message) -> None:
    if actual == expected:
        print(f"Pass: {message}")
    else:
        print(f"Fail: {message}")

def test_reverse_string():
    print("reverse string")
    assert_equal(reverse_string.reverse_string("abc"), "cba", "Basic letters")
    assert_equal(reverse_string.reverse_string("123"), "321", "Basic numbers")
    assert_equal(reverse_string.reverse_string("%^_09i3"), "3i90_^%", "Complex")
    assert_equal(reverse_string.reverse_string("racecar"), "racecar", "Palindrome")

def test_palindrome_checker():
    print("palindrome checker")
    assert_equal(palindrome_checker.palindrome_checker("abc"), False, "Basic letters")
    assert_equal(palindrome_checker.palindrome_checker("123"), False, "Basic numbers")
    assert_equal(palindrome_checker.palindrome_checker("racecar"), True, "Basic palindrome")
    assert_equal(palindrome_checker.palindrome_checker("a1b33b1a"), True, "Complex palindrome")

def test_max_min_in_list():
    print("max/min")
    assert_equal(max_min_in_list.find_min_max([1, 2, 3, 4]), (1, 4), "Basic list")
    assert_equal(max_min_in_list.find_min_max([-4, -3, -2, -1]), (-4, -1), "All negative")

def test_duplicate_remover():
    print("duplicate remover")
    assert_equal(duplicate_remover.remove_duplicates(duplicate_remover.parse_list("h e l l o")), "h e l o","Basic word")
    assert_equal(duplicate_remover.remove_duplicates(duplicate_remover.parse_list("1 2 2 3 4")), "1 2 3 4","Basic list")

def test_fizz_buzz():
    print("fizz buzz")
    assert_equal(fizzbuzz.fizz_buzz(5), ["1", "2", "Fizz", "4", "Buzz"],"Up to 5")
    assert_equal(fizzbuzz.fizz_buzz(1), ["1"],"1")
    assert_equal(fizzbuzz.fizz_buzz(15)[-1], "FizzBuzz","Just 15")

def test_sum_of_digits_of_number():
    print("sum of digits")
    assert_equal(sum_of_digits_of_number.sum_digits(123), 6, "123")
    assert_equal(sum_of_digits_of_number.sum_digits(2), 2, "2")
    assert_equal(sum_of_digits_of_number.sum_digits(10), 1, "10")

def test_merge_sorted_lists():
    print("merge sorted lists")
    assert_equal(merge_sorted_lists.merge_lists([-1, 5, 8], [2, 6, 10]), [-1, 2, 5, 6, 8, 10], "Basic")

def test_second_largest_number():
    print("second largest")
    assert_equal(second_largest_number.get_second_largest_number([2, 3, 4, -3, 9]), 4, "Basic")
    assert_equal(second_largest_number.get_second_largest_number([1, 1, 2, 2, 3, 3]), 2, "Basic")
    assert_equal(second_largest_number.get_second_largest_number([-10, -5, -3, -3]), -5, "Basic")

def test_rotate_string():
    print("rotate string")
    assert_equal(rotate_string.rotate_string("a", 5), "a", "Single letter")
    assert_equal(rotate_string.rotate_string("abcd", 3), "bcda", "Basic")
    assert_equal(rotate_string.rotate_string("abcd", -1), "bcda", "Negative spaces")
    assert_equal(rotate_string.rotate_string("abcd", 0), "abcd", "0 rotation")
    assert_equal(rotate_string.rotate_string("", 4), "", "Empty string")

def test_count_vowels():
    print("count vowels")
    assert_equal(count_vowels.count_vowels("rhythm"), {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0, "total": 0}, "No vowels")
    assert_equal(count_vowels.count_vowels("aEiOu"), {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "total": 5}, "Upper and lower case")
    assert_equal(count_vowels.count_vowels("aAeoUUU"), {"a": 2, "e": 1, "i": 0, "o": 1, "u": 3, "total": 7}, "Upper and lower case")

def test_check_anagram():
    print("check anagram")
    assert_equal(check_anagram.check_anagram("listen", "silent"), True, "listen, silent")
    assert_equal(check_anagram.check_anagram("a b aa", "aaa b"), True, "Random letters")
    assert_equal(check_anagram.check_anagram("Hello", "World"), False, "Basic non-anagram")
    assert_equal(check_anagram.check_anagram("A t om", "m O aTs"), False, "Basic anagram")

def test_validate_balanced_parentheses():
    print("balanced parentheses")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses(""), True, "Empty")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("(a){b}c[]"), True, "letters and brackets")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("({[]})"), True, "Nested parentheses")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("({"), False, "Only open parentheses")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("([)]"), False, "Wrong order")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("}]])"), False, "Only close brackets")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses("(((())))"), True, "Nested balanced parentheses")
    assert_equal(validate_balanced_parentheses.validate_balanced_parentheses(")}{("), False, "Inside out")

def test_binary_search():
    print("binary search")
    assert_equal(binary_search.binary_search([1, 2, 3, 4], 3), 2, "Basic")
    assert_equal(binary_search.binary_search([-3, 4, 8, 10], 5), -1, "Not in list")
    assert_equal(binary_search.binary_search([1], 1), 0, "Single element")
    assert_equal(binary_search.binary_search([1], 2), -1, "Single element not in list")
    assert_equal(binary_search.binary_search([1, 2, 3, 4], 1), 0, "Basic")
    assert_equal(binary_search.binary_search([1, 2, 3, 4], 4), 3, "Basic")
    assert_equal(binary_search.binary_search([-5, -2, 0, 3, 7], -5), 0, "Longer list")
    assert_equal(binary_search.binary_search([-5, -2, 0, 3, 7], 7), 4, "Longer list")

def test_two_sum():
    print("two sum")
    assert_equal(two_sum.calculate_two_sum([1, 2, 3, 4], 5), {1: 4, 2: 3}, "Basic")
    assert_equal(two_sum.calculate_two_sum([-1, 2, -3, 4], -4), {-3: -1}, "Basic")
    assert_equal(two_sum.calculate_two_sum([1, 2, 3, 4], 8), {}, "No sum")
    assert_equal(two_sum.calculate_two_sum([2, 2, 2, 2], 4), {2: 2}, "Homogeneous list")
    assert_equal(two_sum.calculate_two_sum([-2, -2, 4, 4], 2), {-2: 4}, "Basic, with repeated items in list")
    assert_equal(two_sum.calculate_two_sum([], 5), {}, "Empty list")
    assert_equal(two_sum.calculate_two_sum([5], 5), {}, "Single item in list")

def test_compress_string():
    print("compress string")
    assert_equal(compress_string.compress_string("aaabb"), "a3b2", "Basic")
    assert_equal(compress_string.compress_string("a  b"), "a1 2b1", "Basic, with spaces")
    assert_equal(compress_string.compress_string(""), "", "Empty string")
    assert_equal(compress_string.compress_string("a"), "a1", "Single character")
    assert_equal(compress_string.compress_string("aaaa"), "a4", "Same character multiple times")
    assert_equal(compress_string.compress_string("abcd"), "a1b1c1d1", "Basic, one letter each")
    assert_equal(compress_string.compress_string("AAaa"), "A2a2", "Upper and lower case")
    assert_equal(compress_string.compress_string("1112221"), "132311", "Only numbers")

def main():
    test_reverse_string()
    test_palindrome_checker()
    test_max_min_in_list()
    test_duplicate_remover()
    test_fizz_buzz()
    test_sum_of_digits_of_number()
    test_merge_sorted_lists()
    test_second_largest_number()
    test_rotate_string()
    test_count_vowels()
    test_check_anagram()
    test_validate_balanced_parentheses()
    test_binary_search()
    test_two_sum()
    test_compress_string()

if __name__ == "__main__":
    main()

