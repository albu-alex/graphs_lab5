

class AdjacencyMatrixGraph:
    def __init__(self, n):
        """
        :param n: The number of vertices
        """
        self.vertices = n
        self.graph = [[0 for i in range(n)] for j in range(n)]

    def is_edge(self, x, y):
        return y in self.graph[x]

    def add_edge(self, x, y, cost):
        if not self.is_edge(x, y):
            self.graph[x][y] = cost
            self.graph[y][x] = cost

    def minimum_coloring_graph(self):
        visited = [0] * self.vertices

        m = 1
        max_colors = 1

        for i in range(1, self.vertices+1):
            if not visited[i]:
                visited[i] = 1
                queue =