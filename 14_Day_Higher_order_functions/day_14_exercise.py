#map - invokes a callback function on each item
#filter - invokes a callback func on each item with a specified condition and returns a list of items that meets the condition
#reduce - invokes callback on each item and returns a single value

from countries_data import countries

print(countries)

def make_upper(name):
    return name.upper()

countries_upper = map(make_upper, countries)
print(list(countries_upper)) # The returned value from map() (map object) then can be passed to functions like list() (to create a list), set() (to create a set) .  

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def make_squared(num):
    return num**2
squared_nums = map(make_squared, numbers)
print(list(squared_nums))