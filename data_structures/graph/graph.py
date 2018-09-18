from ..queue.queue import Queue


class Graph:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        return 'Graph: {}'.format(self.graph)

    def __str__(self):
        return 'Graph: {}'.format(self.graph)

    def __len__(self):
        return len(self.graph.items())

    def add_vert(self, name):
        """Use val to create new Vertice and add vertice to graph.
        """
        if name not in self.graph:
            self.graph[name] = []
        else:
            return 'Vertex already exists.'

    def has_vert(self, name):
        """Checks for a key in the graph.
        """
        if name in self.graph:
            return True
        else:
            return False

    def add_edge(self, v1, v2, weight=None):
        """Add a relationship and weight between two vertices.
        """
        if self.has_vert(v1) and self.has_vert(v2):
            if weight:
                new_neighbor = {}
                new_neighbor[v2] = weight
                self.graph[v1].append(new_neighbor)
                return True
            else:
                self.graph[v1].append(v2)
        else:
            return False

    def get_neighbors(self, name):
        """Given a name (key), return all adjacent vertices.
        """
        if self.has_vert(name):
            return self.graph[name]
        else:
            raise KeyError

    def breadth_first(self, s):
        """Function that prints Vertex names breadth-wise
        """
        visited = {}
        for k, v in self.graph.items():
            visited[k] = False

        q = Queue()
        q.enqueue(s)
        visited[s] = True

        while q._length:
            s = q.dequeue()
            print(s)
            for n in self.graph[s]:
                try:
                    name = list(n.keys())[0]
                except AttributeError:
                    name = n
                    if not visited[name]:
                        q.enqueue(name)
                        visited[name] = True
