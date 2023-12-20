import math

def add_two_numbers(a, b):
    return a + b

def calc_area_circle(radius):
    return 3.14 * radius**2 

print(calc_area_circle(3))

def add_all_nums(*nums):
    sum = 0
    for num in nums:
        if type(num) != int:
            return print('not able to add non-integer')
        sum += num
    return sum
print(add_all_nums(5, 2, 'hello'))

def check_season(month):
    if month == 'January' or 'February' or 'December':
        return 'Winter'
print(check_season('December'))

def print_list(items):
    for item in items:
        print(item)

def reverse_list(items):
    reversed = items[::-1]
    return reversed
print(reverse_list([1, 2, 3]))

def capitalize_list_items(items):
    capitalized = []
    for item in items:
        capitalized.append(item.capitalize())
    return capitalized
print(capitalize_list_items(['apple', 'peach']))

def add_item(list, item):
    list.append(item)
    return list

def evens_and_odds(num):
    evens = 0
    odds = 0
    for num in range(num):
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    print(f'Evens count is {evens} and Odds count is {odds}')
evens_and_odds(100)

def factorial(num):
    return math.factorial(num)

def is_unique(items):
    length_items = len(items)
    items_set = set(items)
    if length_items == len(items_set):
        return True
    return False
print(is_unique(['apple', 'apple', 'pear']))