python_string = 'Thirty ' + 'Days ' + 'Of ' + 'Python'
print(python_string) # 'Thirty Days Of Python'

company = 'Coding For All'
print(len(company)) # 14

print(company.upper()) # 'CODING FOR ALL'
print(company.lower()) # 'coding for all'
print(company.title()) # 'Coding For All'
print(company.capitalize()) # 'Coding for all'
print(company.swapcase()) # 'cODING fOR aLL'

print(company[0:6]) #Coding
print(company.find('Coding')) # 0
print(company.index('Coding')) # 0
print(company.replace('Coding', 'Python')) # 'Python For All'

print(company.split()) # ['Coding', 'For', 'All']

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

print(company[-1])
print(company[0] + company[7] + company[11]) #CFA

tech_company = 'Coding For All People'
print(tech_company.rfind('l')) # 19

phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase[31:54]) #because because because

print(company.startswith('Coding')) # True
print(company.endswith('coding')) # False

print('30DaysOfPython'.isidentifier()) #False
print('thirty_days_of_python'.isidentifier()) #True

python_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(python_libs))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius 10 is {} meters square'.format(area))

a = 8
b = 6

print('{} + {} = {}'.format(a, b, a + b))