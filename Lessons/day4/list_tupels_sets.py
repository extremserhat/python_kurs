# List Tupels Sets

courses = ['History', 'Physics', 'Math', 'CompSci']

print(f"\nThe list of the courses are: {courses}")

print("How many values are in the list: ", len(courses)) # use len to know the list length

# We have 4 values. Index starts at 0 til to 3.
print("\n List the specific value of this list: ", courses[2]) # list the specific list value

# Negative index -1 -
print("\n List the last item in the list: ", courses[-1])

# Start and endpoint for the index
print(f"\n The courses index have all this values: {courses[0:5]}")
# another way to solve this
print(f"\n the courses index have all this values: {courses}")
# or
print(f"\n the courses index have all this values: {courses[0:]}")

# list methods

courses.append('Art')

print("\n The list are changed: ", courses) # here is a new value

# specific place with INSERT() 
courses.insert(2, 'Music')
print("\n The list are changed again: ", courses) # with insert we can put anywhere we want the new value 

# list in list 
courses_2 = ['Chemistry', 'Biology']
courses.append(courses_2)
print("\n now we have a list in list : ", courses)

courses.insert(2, courses_2)
print("\n now we have a list in list with 2 another lists : ", courses) # here we put the list in the specific place we want


print("\n Now we have a list in the list and we want the ones we put in the certain place to list them: ", courses[2])

courses.extend(courses_2)
courses.remove(courses[-1])
courses.pop(6)
print(courses)

courses.reverse()
print("\n reverse list: ", courses)

item_list = ['fork', 'spoon', 'knife', 'plate', 'cup']
item_list.sort()
print(f"\nThe list of the items: {item_list}")

number_list = [8, 10, 1, 2, 5, 6, 3, 7, 4, 9]

print(number_list)
print('\n',number_list.sort())
print(f"\n {number_list.sort()}")

number_list.sort(reverse=True)
print(number_list)


number_list_1 = [8, 10, 1, 2, 5, 6, 3, 7, 4, 9]

sorted(number_list_1) # makes a sorted version but its not sort
print("sorted funtkion: ",number_list_1)

sorted_nuberlist = sorted(number_list_1) # make a new variable
print("new variable: ",sorted_nuberlist) # now with the new variable if we print that out the list are sorted

print(min(sorted_nuberlist)) #  returns the smallest value

print(max(sorted_nuberlist)) # returns the biggest value
print(sum(sorted_nuberlist)) # returns the sum of the list 

# Good to check if the specific value are in the list
print(courses.index('History')) # returns the index where the History is

# check if art are in the list of courses_2
print('Art' in courses_2) # returns true or false
