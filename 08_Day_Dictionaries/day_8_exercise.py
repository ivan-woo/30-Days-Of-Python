dog = dict()

dog['name'] = 'Stanley'
dog['color'] = 'brown'
dog['legs'] = 4
dog['age'] = 18
dog['breed'] = 'Mixed Corgi'

print(dog)

student = {}
student['first_name'] = 'kevin'
student['last_name'] = 'lee'
student['gender'] = 'male'
student['age'] = 20
student['marital_status'] = 'single'
student['skills'] = ['javascript', 'python', 'sql']
print(len(student)) #6
print(type(student['skills']))
student['skills'].append('css')
print(student.values())
print(student.items()) # dict_items([('first_name', 'kevin'), ('last_name', 'lee'), ('gender', 'male'), ('age', 20), ('marital_status', 'single'), ('skills', ['javascript', 'python', 'sql', 'css'])])

dog.pop('color')
del student
print(student)