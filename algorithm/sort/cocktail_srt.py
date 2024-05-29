from typing import List
import random

# shaker sortともいうらしい
def cocktail(numbers: List[int]) -> List[int]:
    len_nums = len(numbers)
    start = 0
    end = len_nums -1
    swapped = True

    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
        
        # この時点で値の交換がない場合、並び替えの必要がないため終了
        if not swapped:
            break

        # limitの変更
        end = end - 1
        # [4,5,1,8,7,3]の場合、[4,5,1,8,7]を7からソートしていく
        for i in range(end-1, start-1, -1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers

nums = [random.randint(1, 100) for _ in range(1, 10)]
print(nums)
print(cocktail(nums))
