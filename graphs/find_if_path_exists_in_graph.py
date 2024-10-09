class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        explored = set()
        path = []
        adj = defaultdict(set)
        for edge in edges:
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        def dfs(exploring, explored, adj):
            #print(explored)
            if exploring in explored:
                return
            explored.add(exploring)
            if exploring == destination:
                return True
            neighbors = adj[exploring]
            for neighbor in neighbors:
                if neighbor not in explored:
                    dfs(neighbor, explored, adj)
        dfs(source, explored, adj)
        print('done')
        return destination in explored
            


        