#Divisible Sum Pairs
import sys


k = 3
a = [1,3,2,6,1,2]
n = 6
# write your code here
sum = 0
for i in range (0, n):
    child_sum = 0
    for j in range(0,n):
        if (((a[i] + a[j]) % k ==  0) and (j != i)):
            child_sum += 1
    sum += child_sum
print(sum)

        
