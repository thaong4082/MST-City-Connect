###### GRAPH ######
class Graph():
  def __init__(self, filename):
    self.vertices = set()
    self.edges = set()
    # key: tuple of vertices | value: edge weight between the two vertices
    self.edge_weights = {}
    #parent pointers where each index is the node
    self.parent = {}
    self.read_file(filename)

  def read_file(self, filename):
    with open(filename, 'r') as file:

      lines = file.readlines()
      num_lines = len(lines)
      print(f'number of lines in input file: {num_lines}')
  
      for line in lines:
          parts = line.strip().split()  # split line into parts
          edge_id, start_id, end_id, edge_weight = parts
          self.vertices.update([start_id, end_id])
          self.edges.add((start_id, end_id))
          self.edge_weights[(start_id, end_id)] = edge_weight
  
        # Initialize parent pointers
          if start_id not in self.parent:
            self.parent[start_id] = start_id
          if end_id not in self.parent:
            self.parent[end_id] = end_id
      print("Graph completed.")

  ## Recursively find the root that represents x
  def find_set(self, x):
    if self.parent[x] == x:
      return x
    return self.find_set(self.parent[x])

  ## When unioning, update v's parent node to u
  def union(self, u, v):
    u_root = self.find_set(u)
    v_root = self.find_set(v)
    self.parent[v_root] = u_root

  def find_set_boruvka(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find_set_boruvka(self.parent[x])
    return self.parent[x]


#### END OF GRAPH FUNCTIONS####
