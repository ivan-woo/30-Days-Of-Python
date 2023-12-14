#Day 5 exercises

empty_list = []

items = ['dog', 'cat', 'mouse', 'elephant', 'bird']

print(len(items)) #5

print(items[0]) #dog
print(items[2]) #mouse

it_companies = ['Meta', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies)) #6
it_companies[0] = 'Emotive'
print(it_companies)

it_companies.insert(1, 'Ring')
print(it_companies) #['Meta', 'Ring', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True) #['Ring', 'Oracle', 'Microsoft', 'IBM', 'Emotive', 'Apple', 'Amazon']
print(it_companies)

fav_companies = it_companies[0:3] # [Ring, Oracle, Microsoft]
print(fav_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.append('Python')
full_stack.append('SQL')
print(full_stack)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
print(ages[0]) #19
print(ages[9]) #26
median_age = (ages[4] + ages[5]) / 2 #24
print(median_age)