# Write a code get an integer number as input and print the odd and even digits of the number separately.


# Input Description:
# A single line containing an integer.

# Output Description:
# Print the even and odd integers of the integer in a separate line.

# Sample Input :
# 1234
# Sample Output :
# 2 4
# 1 3

a = int(input())

e = [int(i) for i in str(a) if int(i) % 2 == 0]
e.sort()
r = [int(j) for j in str(a) if int(j) % 2 != 0]
r.sort()
print(*e)
print(*r)
