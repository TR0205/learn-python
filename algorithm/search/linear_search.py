from typing import List
import random

def linear_search(numbers: List[int], target: int) -> int:
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1

# numbers = [random.randint(1, 100) for _ in range(1, 10)]
numbers = [0, 1, 5, 7, 9, 11, 15, 20, 24]
# print(linear_search(numbers, 3))

def binary_search(numbers: List[int], target: int) -> int:
    left, right = 0, len(numbers)-1
    while left <= right:
        mid = (left + right)//2
        if numbers[mid] == target:
            return mid
        else:
            if numbers[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1
            

print(binary_search(numbers, 15))