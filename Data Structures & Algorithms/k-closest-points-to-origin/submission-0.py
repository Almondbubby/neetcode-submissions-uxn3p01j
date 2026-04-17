import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        def distance(x, y):
            return ((x ** 2) + (y ** 2))**(1/2)
        
        heap = []
        for i in range(len(points)):
            dist = -distance(points[i][0], points[i][1])
            if len(heap) == k and dist > heap[0][0]:
                heapq.heapreplace(heap, (dist, points[i]))
            elif len(heap) < k:
                heapq.heappush(heap, (dist, points[i]))
        
        return [l[1] for l in heap]