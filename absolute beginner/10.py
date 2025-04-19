# You are provided with a number "N", Find the Nth term of the series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......

# (Print "Error" if N = negative value and 0 if N = 0).


# Input Description:
# An integer N is provided to you as the input.

# Output Description:
# Find the Nth term in the provided series.

# Sample Input :
# 18
# Sample Output :
# 324

a=int(input(""))
b=[]
for i in range (0,1000):
    b.append(i*i)
    i=i+1
if a<0:
    print("Error")
elif a==0:
    print("0")
else:
    print(b[a])
