from typing import List
import random

# n**2
nums = [random.randint(1, 1000) for _ in range(1, 10)]

def bubble_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums) - 1 - i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums
    
print(bubble_sort(nums))
