from graph import *

def kruskal(graph):
    mst = []
    # Sort edges in order of increasing weight
    sorted_edges = sorted(graph.edge_weights.keys(), key=lambda edge: graph.edge_weights[edge])
  # print(sorted_edges)
    for edge in sorted_edges:
        start, end = edge
        weight = graph.edge_weights[edge]
        # If adding edge would not create a cycle
        if graph.find_set(start) != graph.find_set(end):
            mst.append((start, end, weight))
            graph.union(start, end)
        # print("Edge:", edge, "| Weight:", weight)
    # print(mst)
    return mst


# graph = Graph('cal.edge')
# # print("set of vertices:\n", graph.vertices)
# # print("\n")
# # print("set of edges:\n", graph.edges)
# # print("\n")
# # print("set of weights:\n", graph.edge_weights, "\n")
# print("KRUSKAL TESTING:")
# kruskal = kruskal(graph)
