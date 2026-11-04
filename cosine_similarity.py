

import math

list1 = [1,2]
list2 = [2,1]
total = 0
for a,b in zip(list1,list2):
     res = math.sqrt(a ** 2 + b ** 2)
     res1 = a*b + b*a


print(res1)
print(res1/(res * res) )