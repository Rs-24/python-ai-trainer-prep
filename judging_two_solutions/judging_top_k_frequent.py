from typing import List, Dict, Tuple, Callable
import heapq

def top_k_frequent_sort(nums: List[int], k: int) -> List[int]:
    """
    Finds the k most frequent elements in nums (in descending order) and
    returns them in the form of a list of ints
    """
    freqs_dict: Dict[int, int] = {}
    for num in nums:
        freqs_dict[num] = freqs_dict.get(num, 0) + 1
    freqs_items = sorted(freqs_dict.items(), key=lambda item: item[1], reverse=True)
    output: List[int] = [element[0] for element in freqs_items]
    return output[:k]

def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """
    Finds the k most frequent elements in nums (in descending order) and
    returns them in the form of a list of ints
    """
    freqs: Dict[int, int] = {}
    for num in nums:
        freqs[num] = freqs.get(num, 0) + 1
    heap: List[Tuple[int, int]] = []
    for num, freq in freqs.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)            
    output: List[int] = []
    for _ in range(min(k, len(heap))):
        element = heapq.heappop(heap)
        output.append(element[1])
    return output[::-1]

def run_test(f: Callable[[List[int], int], List[int]]) -> None:
    tests = [(([], 1), []), (([1], 2), [1]), (([1, 1, 2, 3, 3, 3, 3], 3), [3, 1, 2]), (([4, 5, 5, 3, 3, 3], 2), [3, 5])]
    for test, expected in tests:
        nums, k = test[0], test[1]
        actual = f(nums, k)
        assert actual == expected, f"{f.__name__}({nums}, {k}) = {actual}, expected {expected}"

def test():
    print("Running tests...")
    run_test(top_k_frequent_sort)
    run_test(top_k_frequent_heap)
    print("All tests passed!")

if __name__ == "__main__":
    test()

# top_k_frequent_sort() review:
# Correctness:
#   - Works for all edge cases, e.g. empty list, single element, k > len(nums), etc
#
# Complexity:
#   - Time: O(n log n) in its worst case, where n = len(nums)
#   - Space: O(n)
#
# Readability:
#   - Very explicit and easy to understand how the algorithm works, also requires fewer lines of code
#
# Use case:
#   - For when teaching/understanding the algorithm are prioritised over time complexity (also, if k ~ n then there may not be a significant time complexity advantage)
#
# top_k_frequent_heap()
# Correctness:
#   - Works for all edge cases, e.g. empty list, single element, k > len(nums), etc
#
# Complexity:
#   - Time: O(n log k), where n = len(nums), and k represents the k most frequent elements in nums
#   - Space: O(n)
#
# Readability:
#   - Not as easy to understand how the algorithm works as it is hidden behind the heap logic, also requires more lines of code
#
# Use case:
#   - For when k << n and/or time complexity is prioritised over teaching/understanding the algorithm
#
# Verdict:
#   - When k ~ n, there is not a significant difference in time complexity, however when k << n,
#     top_k_frequent_heap() takes significantly less time and hence I would advise using this in
#     any production setting
#   - top_k_frequent_sort() is much easier to understand and hence I would advise using it for 
#     teaching/understanding the algorithm. Additionally, if k ~ n, then the time complexities 
#     may be very similar, and in this scenario top_k_frequent_sort() could be used for production
#     if readability is also a priority