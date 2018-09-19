def depth_first(g, root):
    visited = {}
    for k in g.keys():
        visited[k] = False

    def _walk(vertex):
        if not visited[vertex]:
            print(vertex)
            visited[vertex] = True
        for el in g.graph[vertex]:
            if not visited[el]:
                _walk(el)

    _walk(root)
