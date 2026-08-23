#Insert , Append and Extend a list 
Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses.append('Art') #Append at the end
Courses.insert(0, 'Art') #Insert at index 0
Courses.extend(['Education', 'Biology']) #Extend the list with another list

# Extend over Insert. Insert creates a List within a list while Extend adds the elements of the list to the existing list.

Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses2 = ['Education', 'Biology']

Courses.insert(0, Courses2) # Insert creates a list within a list
print(Courses) # Output: [['Education', 'Biology'], 'History', 'Math', 'Physics', 'CompSci']
print(Courses[0]) # Output: ['Education', 'Biology']

Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses.extend(Courses2) # Extend adds the elements of the list to the existing list
print(Courses) # Output: ['History', 'Math', 'Physics', 'CompSci', 'Education', 'Biology']

Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses.append(Courses2) # Append adds the list as a single element at the end of the list
print(Courses) # Output: ['History', 'Math', 'Physics', 'CompSci', ['Education', 'Biology']]

 
#Remove and Pop from a list.
#Pop removes the last element or the element at a specific index and returns it, while remove removes a specific element by value.

Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses.remove('Math') # Remove a specific element, removed math from the list
print(Courses) # Output: ['History', 'Physics', 'CompSci']

Courses.pop() # Remove the last element by default, removed CompSci from the list
print(Courses) # Output: ['History', 'Physics']

Courses.pop(1) # Remove the element at index 1
print(Courses) # Output: ['History']


popped_course = Courses.pop(0) # Remove the element at index 0 and store it in a variable
print(popped_course) # Output: 'History'

#Reverse a list with Function, Slicing and Logic

Courses = ['History', 'Math', 'Physics', 'CompSci']
Courses.reverse() # Reverse the list in place
print(Courses) # Output: ['CompSci', 'Physics', 'Math', 'History']

Courses_Reverse = Courses[::-1] # Reverse the list using slicing
print(Courses_Reverse) # Output: ['CompSci', 'Physics', 'Math', 'History']

#Using logic to reverse a list. Traverse the list in reverse order and append each element to a new list.
Courses = ['History', 'Math', 'Physics', 'CompSci'] 
reversed_courses = []
for i in range(len(Courses) - 1, -1, -1):
    reversed_courses.append(Courses[i])
print(reversed_courses) # Output: ['CompSci', 'Physics', 'Math', 'History']


#Using logic to sort a list. Traverse the list and compare each element with the next element, 
#if the current element is greater than the next element, swap them. Repeat this process until the list is sorted.
Courses = ['History', 'Math', 'Physics', 'CompSci']
for i in range(len(Courses)):
    for j in range(i + 1, len(Courses)):
        if Courses[i] > Courses[j]:
            Courses[i], Courses[j] = Courses[j], Courses[i]
print(Courses) # Output: ['CompSci', 'History', 'Math', 'Physics']

#how to find duplicate elements in a list. 
#Create an empty list to store the duplicates, traverse the original list and check if the element is already in the duplicates list, if not, add it to the duplicates list.
duplicates = []
Courses_D = ['CompSci', 'History', 'Math', 'Physics', 'CompSci', 'History', 'Math', 'Physics']
for element in Courses_D:
    if element in duplicates:
        continue
    if Courses_D.count(element) > 1:
        duplicates.append(element)
print(duplicates) # Output: ['CompSci', 'History', 'Math', 'Physics']

#How to find the index of duplciate elements in a list. 
#Create an empty list to store the indexes, traverse the original list and check if the element is already in the indexes list, if not, add it to the indexes list.

indexes = []
for element in duplicates:
    indexes.append([i for i, x in enumerate(Courses_D) if x == element])
print(indexes) # Output: [[0, 4], [1, 5], [2, 6], [3, 7]]

#2nd way
indexes = []
Courses_D = ['CompSci', 'History', 'Math', 'Physics', 'CompSci', 'History', 'Math', 'Physics']
for i, element in enumerate(Courses_D):
    if element in Courses_D[:i]:
        indexes.append(i)
print(indexes) # Output: [4, 5, 6, 7]