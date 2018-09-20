def depth_first(g, root):
    """Function that, when given a starting vertex, performs a depth-first traversal using a pre-ordered recursive walk function.
    """
    visited = {}
    for k in g.graph.keys():
        visited[k] = False

    def _walk(vertex):
        if not visited[vertex]:
            print(vertex)
            visited[vertex] = True
        for el in g.graph[vertex]:
            if not visited[el]:
                _walk(el)

    _walk(root)
