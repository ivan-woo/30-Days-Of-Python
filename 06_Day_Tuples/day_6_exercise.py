# Tuples

fruits = ('banana', 'orange', 'mango', 'lemon')

print(fruits.count('banana'))

'dog' in fruits # false
'orange' in fruits #true

tpl = tuple()

sisters = ('amy', 'sophia')
brothers = ('kevin', 'josh')
siblings = sisters + brothers
print(siblings)
print(len(siblings)) # 4

family_members = list(siblings)
family_members.append('brenda')
family_members.append('wallace')
family_members = tuple(family_members)
print(family_members)

parents = family_members[4:]
sisters_brothers = family_members[0:4]
print(parents)
print(sisters_brothers)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) #false
print('Iceland' in nordic_countries) #true