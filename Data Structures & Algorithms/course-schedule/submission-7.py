class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in graph:
                graph[prerequisites[i][0]] = [prerequisites[i][1]]
            else:
                graph[prerequisites[i][0]].append(prerequisites[i][1])
            if prerequisites[i][1] not in graph:
                graph[prerequisites[i][1]] = []
        print(graph)


        def dfs(graph, node, courses):
            if node in courses:
                #print(node)
                return False
            courses.add(node)
            for neighbor in graph[node]:
                #print(node, courses)
                result = dfs(graph, neighbor, courses)
                if result is False:
                    return False
            courses.remove(node)
            return True


            
        for node in graph:
            result = dfs(graph, node, set())
            if not result:
                return False
        return True