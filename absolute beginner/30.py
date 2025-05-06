# Write a program to get a string as input and reverse the string without using temporary variable.


# Input Description:
# A single line containing a string.

# Output Description:
# Print the reversed string.

# Sample Input :
# GUVI
# Sample Output :
# IVUG

a1= input()
a = list(a1)
s, e = 0, len(a)-1

while(s<e):
    a[s], a[e] = a[e],a[s]
    s+=1
    e-=1
    
print("".join(a))
