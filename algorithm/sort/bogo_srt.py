import random
from typing import List

# python3からタイプヒントのListを使用できる。その前まではlistだった
def in_order(numbers: List[int]) -> bool:
    # allは全ての要素が真ならTrueを返す
    # 今回だったら[0]と[1]を比較、[1]と[2]を比較・・・でrange分実行し、全てTrueの場合Trueを返す
    # numbers[i] <= numbers[i+1]の比較をrange分実行し、全てTrueでなければならない
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # 以下はfor版
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True

def bogo_sort(numbers: List[int]) -> list[int]:
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers

print(bogo_sort([1,5,3,2,6]))