class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # make graph for courses
        # course -> prereq directed graph
        graph = defaultdict(list)
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])

        # constants for state definitions
        UNSEEN = 0
        VISITING = 1
        VISITED = 2

        # manage states of graph nodes
        # using a list where index is course number
        # value is state of the node
        states = [UNSEEN] * numCourses
        def dfs(course):
            state = states[course]
            if state == VISITING:
                return False
            if state == VISITED:
                return True
            
            states[course] = VISITING
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            states[course] = VISITED
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
    