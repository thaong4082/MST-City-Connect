from graph import *

def prim_mst(graph):
  
  # Empty priority queue, implemented as a list in python
  pq = []  

  # Iterate through all vertices and add them to the priority queue
  for edge, weight in graph.edge_weights.items():
      pq.append((weight, edge))

  # Sort the priority queue in ascending order by weight
  # We are greedily choosing the edges with the lowest weights 
  pq.sort()

  # Start with an empty MST
  mst_edges = []

  # Iterate through everything in the priority queue
  for weight, (u, v) in pq:
    # Check if adding this edge will create a cycle
      if graph.find_set(u) != graph.find_set(v):

        # This edge won't creae a cycle so, add it to the MST
          mst_edges.append((u, v, weight))
          graph.union(u, v)
  
  return mst_edges


