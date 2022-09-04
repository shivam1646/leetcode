class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0

        # calculates manhattan distance
        def dist(u, v):
            x1, y1 = points[u]
            x2, y2 = points[v]
            return abs(x1 - x2) + abs(y1 - y2)
        
        def find(n):
            p = parent[n]
            while p != parent[p]:
                p = parent[p]
            return p
        
        def union(u, v):
            p1 = find(u)
            p2 = find(v)
            
            # cycle found
            if p1 == p2:
                return True
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            
            return False

        n = len(points)
        edge_weight_map = defaultdict(int)
        # connect each pair of points with a weighted edge
        for i in range(0, n):
            for j in range(i + 1, n):
                edge_weight_map[(i, j)] = dist(i, j)

        # sort edges in non-decreasing order by weight
        sorted_edges_list = sorted(edge_weight_map.items(), key = lambda x : x[1])

        parent = [i for i in range(0, n)]
        rank = [1 for _ in range(0, n)]
        
        cost = 0
        edges_count = 0
        
        # Find mst using Kruskal's algo
        for edge, weight in sorted_edges_list:
            u, v = edge
            # pick smallest edge
            # if it forms a cycle(detect using union-find), discard it
            # else include this edge in mst
            if not union(u, v):
                cost += weight
                edges_count += 1
            # mst found
            if edges_count == n - 1:
                return cost
