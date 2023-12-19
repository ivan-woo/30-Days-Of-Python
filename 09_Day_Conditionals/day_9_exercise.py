age = int(input("Enter your age:" ))

if age >= 18:
    print('You are old enough to drive')
else:
    diff = 18 - age
    print(f'You need {diff} more years to learn to drive')

my_age = 29

def age_message(user_age, my_age):
    if age == my_age:
        print('We are the same age!')
    elif age > my_age:
        diff = age - my_age
        print(f'You are older by {diff} {"year" if diff == 1 else "years"}')
    else:
        diff = my_age - age
        print(f'I am older by {diff} {"year" if diff == 1 else "years"}')

age_message(age, my_age)


fruits = ['banana', 'orange', 'mango', 'lemon']

def check_fruits(fruit, fruits_list):
    if fruit in fruits_list:
        print('That fruit already exist in the list')
    else:
        fruits_list.append(fruit)
        print(f'added {fruit} to the list!')

check_fruits('banana', fruits)


person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    print(person['skills'][0])
if person['is_marred'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')