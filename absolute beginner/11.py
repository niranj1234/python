# You are given the coefficients of a quadratic equation in order A, B & C.

# Where A is the coefficient of X2,  B is the coefficient of X and C is the constant term in the most simplified form.

# Example: For  X2 + 5X + 6 = 0, you are given the input as: 1 5 6.

# Write a program to find all of the roots of the quadratic.

# Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

# Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a


# Input Description:
# Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

# Output Description:
# Print the two values of X after rounding off to 2 decimal places if required.

# Sample Input :
# 1 5 6
# Sample Output :
# -2.00
# -3.00


a, b, c = map(int, input().split())

discriminant = b**2 - 4*a*c

if discriminant >= 0:  # Handle both positive and zero discriminant cases
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5)/(2*a)

    print("{:.2f}".format(root1))
    if discriminant != 0: # Avoid printing the same root twice when discriminant is zero
        print("{:.2f}".format(root2))
