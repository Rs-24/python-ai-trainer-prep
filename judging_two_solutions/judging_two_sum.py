from typing import List, Dict

def calculate_two_sum_complex(nums: List[int], num: int) -> Dict[int, int]:
    pairs: Dict[int, int] = {}
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == num and i != j:
                if nums[i] not in pairs and nums[i] not in pairs.values():
                    if nums[i] < nums[j]:
                        pairs[nums[i]] = nums[j]
                    else:
                        pairs[nums[j]] = nums[i]
    return pairs

def calculate_two_sum_best(nums: List[int], num: int) -> Dict[int, int]:
    pairs: Dict[int, int] = {}
    seen = set()
    for n1 in nums:
        n2 = num - n1
        if n2 in seen:
            if n1 not in pairs and n1 not in pairs.values():
                if n1 < n2:
                    pairs[n1] = n2
                else:
                    pairs[n2] = n1
        seen.add(n1)
    return pairs

def test():
    print("Running tests...")

    assert calculate_two_sum_complex([1, 2, 3, 4], 5) == {1: 4, 2: 3}
    assert calculate_two_sum_best([1, 2, 3, 4], 5) == {1: 4, 2: 3}

    assert calculate_two_sum_complex([-1, 2, -3, 4], -4) == {-3: -1}
    assert calculate_two_sum_best([-1, 2, -3, 4], -4) == {-3: -1}

    assert calculate_two_sum_complex([1, 2, 3, 4], 8) == {}
    assert calculate_two_sum_best([1, 2, 3, 4], 8) == {}

    assert calculate_two_sum_complex([2, 2, 2, 2], 4) == {2: 2}
    assert calculate_two_sum_best([2, 2, 2, 2], 4) == {2: 2}

    assert calculate_two_sum_complex([-2, -2, 4, 4], 2) == {-2: 4}
    assert calculate_two_sum_best([-2, -2, 4, 4], 2) == {-2: 4}

    assert calculate_two_sum_complex([], 5) == {}
    assert calculate_two_sum_best([], 5) == {}

    assert calculate_two_sum_complex([5], 5) == {}
    assert calculate_two_sum_best([5], 5) == {}

    print("All tests passed!")

if __name__ == "__main__":
    test()

# calculate_two_sum_complex() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(N^2), where N = len(nums)
#   - Space: O(N), where N = len(nums), mainly from pairs dictionary
#
# Readability:
#   - More complex than calculate_two_sum_best(), but easier to understand how the algorithm works
#
# Use case:
#   - For when teaching and helping people understand the algorithm is prioritised over readability

# calculate_two_sum_best() review:
# Correctness:
#   - Works for all edge cases
#
# Complexity:
#   - Time: O(N), where N = len(nums)
#   - Space: O(N), where N = len(nums), mainly from pairs dictionary
#
# Readability:
#   - Not as complex as calculate_two_sum_complex()
#
# Use case:
#   - For when readability is prioritised over teaching/understanding of the algorithm