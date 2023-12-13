# Day2: 30 Days of python programming

first_name = 'Ivan'
last_name = 'Woo'
full_name = 'Ivan Woo'
country = 'USA'
city = 'Los Angeles'
age = 21
year = 2023
is_married = False
is_true = True
is_light_on = False
car_make, car_model, car_year = 'Honda', 'Accord', 2023

print(type(first_name)) #string
print(type(last_name)) #string
type(full_name) #string
type(country) #string
type(city) #string
print(type(age)) #int
type(year) #int
type(is_married) #boolean
type(is_true) #boolean
print(type(is_light_on)) #boolean
type(car_make) #string
type(car_model) #string
type(car_year) #int

print(len(first_name)) # 4
print(len(first_name) > len(last_name)) # True

num_one = 5
num_two = 4

total = num_one + num_two # 9
diff = num_one - num_two # 1
prod = num_one * num_two # 20
div = num_one / num_two # 1.25
remainder = num_one % num_two # 1
exp = num_one**num_two #625
floor_div = num_one // num_two #1

print(div)
print(remainder)
print(exp)
print(floor_div)

radius = 30
area_of_circle = 3.14 * (30^2)
print(area_of_circle)

first_name = input('What is your first name? ')
print(first_name) 
print(first_name) # whatever user inputs
last_name = input('What is your last name? ')
print(last_name)
print(last_name)