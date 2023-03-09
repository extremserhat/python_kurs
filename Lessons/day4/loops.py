# loops

courses = ['History', 'Math', 'Physics', 'CompSci']

for item in courses:
    print(item)

for index in enumerate(courses):
    print(index) # returns:
"""
(0, 'History')
(1, 'Math')
(2, 'Physics')
(3, 'CompSci')

"""
for index, items in enumerate(courses):
    print(index, items) # returns:
"""
0 History
1 Math
2 Physics
3 CompSci

"""
for index, items in enumerate(courses, start=1):
    print(f"\nthe index: {index} and the value: {items}") # returns:
"""
# The index starts with 1
he index: 1 and the value: History

the index: 2 and the value: Math

the index: 3 and the value: Physics

the index: 4 and the value: CompSci

"""

courses_str = ", \n".join(courses)

while True:
    print(f"{courses_str}")
    break

new_list = courses_str.split(" \n") # split the \n
print("the new list: ", new_list)

fruit_list = ['Appel', 'Berry', 'Banana', 'Fig', 'Cherry', 'Apricot', 'Kiwi', 'Iychee', 'Mandarin', 'Melon', 'Pineapple', 'Plum']
new_fruit_list = fruit_list

fruit_list[0] = 'Lemon'

print("\n The first fruit list: " , fruit_list)
print("\n The second fruit list: ", new_fruit_list)

# Tuple  -  Mutable

tuple_1 = ('Mercedes', 'Audi', 'Volkswagen', 'Dodge Ram', 'Hiyundai', 'Opel', 'Ford', 'Togg')
tuple_2 = tuple_1

print("\n Tupel 1: ", tuple_1)
print("\n tuple_2: ", tuple_2)

# To assign a new value is not possible
# Tuple is unmutable
"""
tuple_1[0] = 'Skoda'
print("\n tuple_1 with Skoda: ", tuple_1)
print("\n tuple_2: ", tuple_2)


line 65, in <module>
    tuple_1[0] = 'Skoda'
TypeError: 'tuple' object does not support item assignment
"""

# Sets
drinks = {'Cola', 'Fanta', 'Ayran', 'Tea', 'Coffee', 'Water', 'Red Bull', 'Sirup'}
drinks_2 = {'Cola', 'Juice', 'Red Bull', 'Smoothie', 'Water', 'Ayran'}

print(f"\n drinks in the list: {drinks}")

# dubplicate dont schow in the print
drinks_dup = {'Cola', 'Fanta', 'Ayran', 'Tea', 'Coffee', 'Water', 'Red Bull', 'Sirup', 'Ayran'}

print(f"\n in the drinks_dup is Ayran dubplicate: {drinks_dup}")

print('Cola' in drinks_dup)

print(drinks.intersection(drinks_2)) #  only shows the same values contained in both lists

print(drinks.difference(drinks_2)) # show the different value

print(drinks.union(drinks_dup)) # show both lists in one array
new_drinklist = drinks_2.union(drinks)
print(new_drinklist)

# Empty_List 
empty_list = []
empty_list = list() 

# Empty_Tupel
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # this isnt right !! Its a dict
empty_set = set()
