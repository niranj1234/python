# Let "A"  be a string. Remove all the whitespaces and find it's length.


# Input Description:
# A string is provide as an input

# Output Description:
# Remove all the whitespaces and then print the length of the remaining string.

# Sample Input :
# Lorem Ipsum
# Sample Output :
# 10

input_string = input()
string_without_spaces = input_string.replace(" ", "")
length = len(string_without_spaces)
print(length)
