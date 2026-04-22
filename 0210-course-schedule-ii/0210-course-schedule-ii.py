from collections import deque
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        indegree = [0] * n
        for a, b in prerequisites:
            adj[b].append(a)
            indegree[a] += 1
        q = deque([i for i in range(n) if indegree[i] == 0])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node)
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)

        return ans if len(ans) == n else []
        