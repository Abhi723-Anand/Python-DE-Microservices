# This list will store integer type elements
arr = [1, 2, 3, 4, 5]

# This list will store character type elements (strings in Python)
arr = ['a', 'b', 'c', 'd', 'e']

# This list will store float type elements
arr = [1.4, 2.0, 24.0, 5.0, 0.0]  # All float values

#forward traversal of an array
#take array input from user
arr = list(map(float, input("Enter elements of the array separated by space: ").split()))

for i in range(len(arr)):   
    print(arr[i], end=" ")  # Output: 1.4 2.0 24.0 5.0 0.0  

#backward traversal of an array
#take array input from user
arr = list(map(float, input("Enter elements of the array separated by space: ").split()))
for i in range(len(arr) - 1, -1, -1):
    print(arr[i], end=" ")  # Output: 0.0 5.0 24.0 2.0 1.4  
