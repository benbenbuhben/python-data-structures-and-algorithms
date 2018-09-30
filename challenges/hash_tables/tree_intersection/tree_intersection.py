from data_structures.hash_table.hash_table import HashTable


def tree_intersection(tree1, tree2):
    h = HashTable(allow_collsions=False)
    common_nodes = []
    nodes1 = tree1.pre_order()
    for node in nodes1:
        h._set(node)
    nodes2 = tree2.pre_order()
    for node in nodes2:
        if h._get(node):
            common_nodes.append(node)
    return common_nodes
