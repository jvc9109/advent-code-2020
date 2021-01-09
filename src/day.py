import numpy as np

def find_two_numbers_criteria(data):
    numbers = [int(i) for i in data.split("\n")[:-1]]
    seen = set()
    for i in numbers:
        rem = 2020 - i
        seen.add(i)
        if rem in seen:
            product = i * rem
            print(product)

def find_three_numbers(data):
    numbers = [int(i) for i in data.split("\n")[:-1]]
    for i in range(len(numbers)):
        rem = 2020 - numbers[i]
        seen = set()
        for j in range(i, len(numbers)):
            seen.add(numbers[j])
            if rem - numbers[j] in seen:
                product = numbers[i] * numbers[j] * (rem - numbers[j])
                print(product)


with open("../data/day1.txt") as file:
    data = file.read()
    result1 = find_two_numbers_criteria(data)
    result2 = find_three_numbers(data)