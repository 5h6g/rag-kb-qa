

import math


def cosine_similarity(x,y):
        total1 = 0
        total2 = 0
        total = 0
        for a,b in zip(x,y):
            total1 += a ** 2
            total2 += b ** 2
            total += a * b
        res = total/(math.sqrt(total1) * math.sqrt(total2))
        return res
v1 = [1,2]
v2 = [2,1]
print(cosine_similarity(v1,v2))
v3 = [1,2,3]
v4 = [1,0,0]
print(cosine_similarity(v3,v4))
v5 = [1,2]
v6 = [1,2]
print(cosine_similarity(v5,v6))
v7 = [1,2]
v8 = [1,1]
print(cosine_similarity(v7,v8))
'''print(math.sqrt(total1) * math.sqrt(total2))
print(total)
print(total/(math.sqrt(total1) * math.sqrt(total2)))'''