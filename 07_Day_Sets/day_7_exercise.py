# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies)) #7
it_companies.add('Twitter')
it_companies.update(['Snowflake', 'Salesforce'])
it_companies.remove('Amazon')
#remove will give an error if item isn't found, discard will not
print(it_companies)
C = A.union(B)
print(C) # {19, 20, 22, 24, 25, 26, 27, 28}
print(A.intersection(B)) # {19, 20, 22, 24, 25, 26}
print(A.issubset(B)) #true
print(A.symmetric_difference(B)) # {27, 28}
del A
del B

age_set = set(age)
print(len(age_set) < len(age)) #true
# list - mutable, ordered, duplicates, 
# tuple - immutable, ordered, round brackets
# set - unique items, unordered, curly braces

sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split()
print(words)
sentence_set = set(words)
print(len(sentence_set)) # 10