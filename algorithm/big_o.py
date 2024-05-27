from typing import List

# Big O notation: https://amdlaboratory.com/amdblog/python%E3%81%A7%E5%AD%A6%E3%81%B6%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E3%81%A8big-o-notationbig-o-%E8%A8%98%E6%B3%95/

# O(1)
# どれだけリストの要素数が増えても、計算量は変わらない
def func1(numbers: List[int]) -> None:
    print(numbers[0])

# func1([1, 2, 3, 4, 5])

# 数が大きくなるほど処理数が増えるが、ある一定を超えると増加量が緩やかになる
# O(log(n))
def func2(n: int) -> None:
    if n <= 1:
        return
    else:
        print(n)
        func2(n/2)

# func2(10000)

# O(n)
# 数が増える量に比例して計算量も増えていく
def func3(numbers: List[int]) -> None:
    for num in numbers:
        print(num)

# func3([1,2,3,4,5,6,7,8,9,10])

# O(n * log(n))
def func4(n: int) -> None:
    for i in range(int(n)):
        print(i, end=' ')
    print()

    if n <= 1:
        return
    func4(n/2)

# func4(20)

# O(n**2)
# n^2ずつ増えていく
def func5(numbers: List[int]) -> None:
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])
        print()

func5([1,2,3,4,5,6,7,8,9,10])
