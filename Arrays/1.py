# You are given with an array of numbers, Your task is to print the difference of indices of largest and smallest number.All number are unique.


# Input Description:
# First line contains a number ‘n’. Then next line contains n space separated numbers.

# Output Description:
# Print the difference of indices of largest and smallest array

# Sample Input :
# 5
# 1 6 4 0 3
# Sample Output :
# -2

n = int(input())
arr = list(map(int, input().split()))

largest = arr[0]
smallest = arr[0]
largest_index = 0
smallest_index = 0

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]
        largest_index = i
    if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i

difference = largest_index - smallest_index
print(difference)
