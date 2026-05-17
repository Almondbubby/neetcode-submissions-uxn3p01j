import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for i in range(len(times)):
            if times[i][0] not in graph:
                graph[times[i][0]] = [(times[i][1], times[i][2])]
            else:
                graph[times[i][0]].append((times[i][1], times[i][2]))
            if times[i][1] not in graph:
                graph[times[i][1]] = []
            
        heap = [(0, k)]
        distances = {}
        while heap:
            dist, node = heapq.heappop(heap)
            if node in distances:
                continue
            distances[node] = dist
            for neighbor, weight in graph[node]:
                if neighbor in distances: continue
                heapq.heappush(heap, (dist + weight, neighbor))
        if len(distances) < n: return -1
        return max(distances.values())