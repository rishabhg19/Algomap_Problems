class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])
        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        states = [UNSEEN] * numCourses
        path = []

        def dfs(node):
            state = states[node]
            if state == VISITED:
                return True
            elif state == VISITING:
                return False
            neighbors = graph[node]
            states[node] = VISITING
            for neighbor in neighbors:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            path.append(node)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        print(path)
        return path

        