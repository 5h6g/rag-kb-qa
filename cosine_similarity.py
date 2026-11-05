

import math

list1 = [1,2]
list2 = [2,1]
total1 = 0
total2 = 0
total = 0
for a,b in zip(list1,list2):
     total1 += a ** 2
     total2 += b ** 2
     total += a * b

print(math.sqrt(total1) * math.sqrt(total2))
print(total)
print(total/(math.sqrt(total1) * math.sqrt(total2)))