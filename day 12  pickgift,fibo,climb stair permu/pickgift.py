import heapq
from math import floor,sqrt
def pick_gift(gifts,k):
    gifts=[-i for i in gifts]
    heapq.heapify(gifts)
    for i in range(k):
        a=-heapq.heappop(gifts)
        heapq.heappush(gifts,-floor(sqrt(a)))
    return -sum(gifts)



print(pick_gift([1,2,3,4,20],2))
