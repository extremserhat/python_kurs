student = {
        'name': 'John', 
        'age': 20,
        'courses': ['Math', 'CompSci']
        }
print(student)

print(f"acces to the name of the student: {student['name']}")

student_key = {
        1 : 'John', 
        'age': 20,
        'courses': ['Math', 'CompSci']
        }
print(f"\n {student_key[1]}")

# is possible to check and dont get a keyvalue error
print(student.get('phone')) # None
# if we want we can modified
print(student.get('phone', 'Not Found'))

# Add that phone number to the dictionary
student['phone'] = '555555-555555'
print(student)

# update the dictionary

student.update({'name': 'Pascal', 'age': 22, 'courses': ['Math', 'CompSci'], 'phone': '33333-33333'})
print(student)
del student['phone']
print('\n delete phone ', student)

age = student.pop('age')
print(age)
print(student)

print(student.keys()) # show the key 
print(student.values()) # show the value
print(student.items()) # show all in the dic

for key, value in student.items():
    print(f"\n the keys: {key}, the values: {value}")
