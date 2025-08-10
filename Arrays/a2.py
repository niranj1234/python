# You are given an array of ids of prisoners. The jail authority found that there are some prisoners of same id. Your task is to help the authority in finding the common ids.


# Input Description:
# First line contains a number ‘n’ representing no of prisoners. Next line contains n space separated numbers.

# Output Description:
# Print the ids which are not unique. Print -1 if all ids are unique

# Sample Input :
# 7
# 1 1 11 121 131 141 98
# Sample Output :
# 1

n = int(input())                               # O(1)
nspace = list(map(int, input().split()))[:n]   # O(n)

for i in range(n):                             # Loop runs up to n times
    a = nspace[i]                              # O(1)
    nspace.pop(i)                              # O(n) — removing by index shifts elements
    if (a in nspace):                          # O(n) — "in" does a linear scan
        print(a)                               # O(1)
        break                                  # Exit loop


# better solution
# seen = set()
# for x in arr:
#     if x in seen:    # O(1) average, hash lookup
#         print(x)
#         break
#     seen.add(x)      # O(1) average, hash insert


'''
Worst-case scenario
The loop could run n times if the break never happens early.
Inside each iteration: pop(i) → O(n)
                      a in nspace → O(n)

                      Together per iteration → O(n + n) = O(n)

Worst-case time: O(n × n) = O(n²)

Best-case scenario
If the duplicate is found at i = 0:
    1 iteration, pop = O(n), in = O(n) → O(n) total.

Space Complexity
nspace list stores n integers → O(n)
Only a few extra variables (a, i) → O(1)
Total space: O(n)
'''
