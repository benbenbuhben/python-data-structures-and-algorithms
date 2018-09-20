
def get_edges(graph, itinerary):
    """Function that takes in a graph and a itinerary in the form of a list. Returns whether the itinerary is possible with only direct flights.
    """
    total_cost = 0

    for i in range(len(itinerary)-1):
        # import pdb; pdb.set_trace()
        if not (graph.has_vert(itinerary[i]) and graph.has_vert(itinerary[i+1])):
            return False
        elif itinerary[i+1] not in graph.get_neighbors(itinerary[i]):
            return False
        else:
            for tuple in graph.graph[itinerary[i]]:
                if list(tuple.keys())[0] == itinerary[i+1]:
                    total_cost += list(tuple.values())[0]

    return 'TRRRRRRRRUUUUUUUUEEEEEEEE!!!!!!!!!! btw, total cost is {}'.format(total_cost)

