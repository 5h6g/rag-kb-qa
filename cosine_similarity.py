

import math


def cosine_similarity(a,b):
        list1 = [1, 2, 3]
        list2 = [1, 0, 0]
        total1 = 0
        total2 = 0
        total = 0
        for a,b in zip(list1,list2):
            total1 += a ** 2
            total2 += b ** 2
            total += a * b
        res = math.sqrt(total1) * math.sqrt(total2)
        return res
print(cosine_similarity(0.8,1.0))
print(cosine_similarity(0.9487,0.2673))



'''print(math.sqrt(total1) * math.sqrt(total2))
print(total)
print(total/(math.sqrt(total1) * math.sqrt(total2)))'''