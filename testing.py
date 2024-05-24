from prims import prim_mst
from interface import Graph, export_mst_to_file

# Testing Prims
print("Testing Prim's algorithm...")
filename = "data/test.cedge"
graph = Graph(filename)
prims = prim_mst(graph)
print("Prim's complete.")
export_mst_to_file(prims, 'test-output/prims-test.cedge')
print("Output is exported") # works, at least with the small test file

# Calculate the weight of the minimum spanning tree
def calc_weight(filename):
  total_weight = 0
  with open(filename, 'r') as file:

    lines = file.readlines()
    num_edges = len(lines)
    print(f'number of edges in MST file: {num_edges}')

    
    for line in lines:
      parts = line.strip().split()  # split line into parts
      edge_id, start_id, end_id, edge_weight = parts
      edge_weight = int(edge_weight)
      total_weight = total_weight + edge_weight
  return total_weight

prim_mst_weight = calc_weight('test-output/prims-test.cedge')
print(f'Prim\'s MST weight: {prim_mst_weight}')

# Testing Kruskal's
# filename = "data/cal.cedge"
# print("in main")
# graph = Graph(filename)
# print("Testing kruskal...")
# kruskal = kruskal(graph)
# print("Kruskal complete")
# export_mst_to_file(kruskal, 'output/kruskal_output_cal.cedge')
# print("Output is exported")
  