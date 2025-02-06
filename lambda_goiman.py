from functools import reduce

def square_numbers(numbers: list) -> list:
    return list(map(lambda num: num ** 2, numbers))

def filter_even_numbers(numbers: list) -> list:
    return list(filter(lambda num: num % 2 == 0, numbers))

def multiply_numbers(numbers: list) -> int:
    return reduce(lambda x, y: x * y, numbers)  

def sum_of_squares_of_even_numbers(numbers: list) -> int:
    return reduce(lambda x, y: x + y, 
                  map(lambda num: num ** 2, filter(lambda num: num % 2 == 0, numbers)), 
)  


print(square_numbers([5, 11]))

print(filter_even_numbers([10, 15, 16, 70, 8]))

print(multiply_numbers([3, 7]))

print(sum_of_squares_of_even_numbers([2, 4, 11]))


