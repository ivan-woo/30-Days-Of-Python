# Day 3: 30 Days of Python

age = 25
height = 5.7
complex_num = 3 + 7j

enter_height = input('Enter a height: ')
enter_base = input('Enter a base: ')
area_of_triangle = int(enter_height) * int(enter_base) * 0.5
print(f'The area of the triangle is: {area_of_triangle}')

enter_side_a = int(input('Enter side a: '))
enter_side_b = int(input('Enter side b: '))
enter_side_c = int(input('Enter side c: '))
perimeter_triangle = enter_side_a + enter_side_b + enter_side_c
print(f'The perimeter of the triangle is: {perimeter_triangle}')

enter_width = int(input('Enter width: '))
enter_length = int(input('Enter a lenght: '))
area_rectangle = enter_width * enter_length
print(area_rectangle)
perimeter_rectangle = (enter_width + enter_length) * 2
print(perimeter_rectangle)

equation = '2x - 2'
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope

print(len('python') > len('dragon')) #false
print('on' in 'python' and 'on' in 'dragon') #true
print('jargon' in 'I hope this fourse is not full of jargon') #true
print('on' not in 'python' and 'on' not in 'dragon') #false
print(str(float(len('python')))) # 6 -> 6.0 -> '6.0'
print(6 % 2 == 0) #true
print(7 // 3 == int(2.7)) #true
print(type('10') == type(10)) #false
#print(int('9.8') == 10) #error - have to convert back to float first
print(float('9.8') == 10) #false