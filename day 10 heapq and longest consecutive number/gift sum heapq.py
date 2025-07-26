import heapq
from math import sqrt, floor

def pick(gifts,k):
    gifts=[ -i for i  in gifts]
    
    heapq.heapify(gifts)
    print(gifts)
    for i in range(k):
        a=-heapq.heappop(gifts)
        print(a)
        heapq.heappush(gifts, -floor(sqrt(a)))
        print(gifts)
    return -sum(gifts)




a=pick([1, 2, 34, 10000], 3)
print(a)
