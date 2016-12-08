graph_unsorted = [(2, []),
                  (5, [11]),
                  (11, [2, 9, 10]),
                  (7, [11, 8]),
                  (9, []),
                  (10, []),
                  (8, [9]),
                  (3, [10, 8])]


def topological_sort(g):
    sorted_vertices = []
    graph_set = dict(g)
    incoming = {inc : 0 for inc in graph_set}
    for e in g:
        for v in e[1]:
            incoming[v] += 1
    zero_inc = []
    for v in incoming:
        if incoming[v] == 0:
            zero_inc.append(v)
    while zero_inc:
        v = zero_inc.pop()
        sorted_vertices.append(v)
        for node in graph_set[v]:
            incoming[node] -= 1
            if incoming[node] == 0:
                zero_inc.append(node)
    if len(sorted_vertices) == len(g):
        return sorted_vertices
    else:
        raise RuntimeError('There is a cycle')

def all_topological_sorts(g):
    results = []
    graph_set = dict(g)
    incoming = {inc : 0 for inc in graph_set}
    for e in g:
        for v in e[1]:
            incoming[v] += 1
    zero_inc = []
    for v in incoming:
        if incoming[v] == 0:
            zero_inc.append(v)
    sort_permutations([], zero_inc, incoming, graph_set, results)
    print results

def sort_permutations(sorted_nodes, zero_inc, incoming, graph_set, results):
    if not zero_inc:
        results.append(sorted_nodes)
    for node in zero_inc:
        sorted_nodes_copy = list(sorted_nodes)
        sorted_nodes_copy.append(node)
        zero_inc_copy = list(zero_inc)
        zero_inc_copy.remove(node)
        incoming_copy = dict(incoming)
        for connection in graph_set[node]:
            incoming_copy[connection] -= 1
            if incoming_copy[connection] == 0:
                zero_inc_copy.append(connection)
        sort_permutations(sorted_nodes_copy, zero_inc_copy, incoming_copy, graph_set, results)

all_topological_sorts(graph_unsorted)
