# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.


# Input Description:
# A single line containing 2 integers separated by space.

# Output Description:
# Print the HCF of the integers.

# Sample Input :
# 2 3
# Sample Output :
# 1

def find_hcf(a, b):
    """Finds the HCF of two integers without recursion or Euclidean algorithm."""

    if a == 0:
        return b
    if b == 0:
        return a

    # Find the smaller number
    smaller = min(a, b)

    hcf = 1  # Initialize HCF to 1 (1 is always a common factor)

    for i in range(1, smaller + 1):  # Iterate from 1 to the smaller number
        if a % i == 0 and b % i == 0:  # Check if i divides both a and b
            hcf = i  # Update HCF if a larger common factor is found

    return hcf

# Get input and convert to integers
num1, num2 = map(int, input().split())

# Calculate and print the HCF
result = find_hcf(num1, num2)
print(result)
