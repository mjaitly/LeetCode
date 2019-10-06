# Runs in Python 2
'''
Given an underected connected graph with n nodes labeled 1..n. A bridge (cut edge) is defined as an edge which, when removed, makes the graph disconnected (or more precisely, increases the number of connected components in the graph). Equivalently, an edge is a bridge if and only if it is not contained in any cycle. The task is to find all bridges in the given graph. Output an empty list if there are no bridges.

Input:

n, an int representing the total number of nodes.
edges, a list of pairs of integers representing the nodes connected by an edge.
Example 1:

Input: n = 5, edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]

Output: [[1, 2], [4, 5]]
Explanation:
There are 2 bridges:
1. Between node 1 and 2
2. Between node 4 and 5
If we remove these edges, then the graph will be disconnected.
If we remove any of the remaining edges, the graph will remain connected.
Example 2:

Input: n = 6, edges = [[1, 2], [1, 3], [2, 3], [2, 4], [2, 5], [4, 6], [5, 6]]

Output: []
Explanation:
We can remove any edge, the graph will remain connected.
Example 3:

Input: n = 9, edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]

Output: [[3, 4], [3, 6], [4, 5]]
'''
from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = defaultdict(list)
        for v in connections:
            graph[v[0]].append(v[1])
            graph[v[1]].append(v[0])

        disc = [None for _ in range(n+1)]
        low = [None for _ in range(n+1)]

        self.time = 0
        res = []

        def dfs(node, parent):
            if disc[node] is None:
                disc[node] = self.time
                low[node] = self.time
                self.time += 1
                for n in graph[node]:
                    if disc[n] is None:
                        dfs(n, node)
                if parent is not None:
                    l = min([low[i] for i in graph[node] if i!=parent]+[low[node]])
                else:
                    l = min(low[i] for i in graph[node]+[low[node]])
                low[node] = l

        dfs(1, None)

        for v in connections:
            if disc[v[0]]<low[v[1]] or disc[v[1]]<low[v[0]]:
                res.append(v)

        return res

if __name__ == '__main__':
    n = 5
    edges = [[1, 2], [1, 3], [3, 4], [1, 4], [4, 5]]
    # n = 9
    # edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 6], [4, 5], [6, 7], [6, 9], [7, 8], [8, 9]]
    solution = Solution()
    print(solution.criticalConnections(n, edges))
