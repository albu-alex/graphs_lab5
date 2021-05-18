

class DictionaryGraph:
    def __init__(self, n):
        """
        :param n: The number of vertices
        """
        self.vertices = n
        self.graph = {}
        self.colours = {}
        for i in range(n):
            self.graph[i] = []
            self.colours[i] = 1

    def is_edge(self, x, y):
        return y in self.graph[x]

    def add_edge(self, x, y):
        if not self.is_edge(x, y):
            self.graph[x].append(y)
            self.graph[y].append(x)

    def minimum_coloring_graph(self):
        visited = [0] * self.vertices

        max_colors = 1

        for i in range(self.vertices):
            if not visited[i]:
                visited[i] = 1
                queue = [i]
                while queue:
                    current_vertex = queue.pop(0)
                    for j in self.graph[current_vertex]:
                        if self.colours[current_vertex] == self.colours[j]:
                            self.colours[j] += 1
                        max_colors = max(max_colors, max(self.colours[current_vertex], self.colours[j]))

                        if not visited[j]:
                            visited[j] = 1
                            queue.append(j)

        print(max_colors)


class MainProgram:
    def __init__(self):
        file = open("input.txt", "r")
        number_of_vertices, number_of_edges = map(int, file.readline().split())
        self.g = DictionaryGraph(int(number_of_vertices))

        for edge in range(number_of_edges):
            x, y = map(int, file.readline().split())
            self.g.add_edge(x, y)

    def run(self):
        self.g.minimum_coloring_graph()


program = MainProgram()
program.run()
