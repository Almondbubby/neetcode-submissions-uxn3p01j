from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        graph = {}
        for i in range(len(wordList)):
            word = wordList[i]
            if word not in graph:
                graph[wordList[i]] = []
            for w in graph:
                differences = 0
                for j in range(len(w)):
                    if word[j] != w[j]:
                        differences += 1
                        if differences > 1:
                            break
                if differences == 1:
                    graph[word].append(w)
                    graph[w].append(word)

        # do bfs to find if you can reach from beginWord to endWord
        q = deque()
        q.append((beginWord, 0))

        visited = set()

        while q:
            cur, depth = q.popleft()
            if cur in visited:
                continue
            depth += 1
            visited.add(cur)
            if cur == endWord:
                return depth
            for neighbor in graph[cur]:
                q.append((neighbor, depth))
        return 0

                