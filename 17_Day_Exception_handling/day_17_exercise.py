#try except === try catch in javascript

"""
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

Can handle via typeerrors
"""

# destructuring using * vs ... for javascript

def sum_of_five_nums(a, b, c, d, e = 2):
    return a + b + c + d + e

lst = [1, 2, 3, 4]
print(sum_of_five_nums(*lst))  # 15

numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers))

def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']

*nordic_countries, Estonia, Russia = names

print(nordic_countries)
print(Estonia)
print(Russia)