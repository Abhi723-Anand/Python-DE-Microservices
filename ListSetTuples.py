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
print(Courses) # Output: ['History', 'CompSci']

popped_course = Courses.pop(0) # Remove the element at index 0 and store it in a variable
print(popped_course) # Output: 'History'