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


arr = list(map(float, input("Enter elements of the array separated by space: ").split())) 
def simpleArraySum(ar):
    total = 0
    for number in ar:
        total += number
    return total

total = simpleArraySum(arr)
print("Sum:", total)

print("Elements:")
for number in arr:
    print(number)


# A Very Big Sum challenge solution
def aVeryBigSum(ar):
    """Return the sum of the integers in ar."""
    return sum(ar)
def diagonalDifference(arr):
    n = len(arr)
    left_to_right = sum(arr[i][i] for i in range(n))
    right_to_left = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(left_to_right - right_to_left)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split()))
    print(aVeryBigSum(arr))
    print("Diagonal Difference:", diagonalDifference([[1, 2, 3], [4, 5, 6], [9, 8, 9]]))