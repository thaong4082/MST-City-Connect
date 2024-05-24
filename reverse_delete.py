class UnionFind:

  def __init__(self, vertices):
    self.parent = {v: v for v in vertices}
    self.rank = {v: 0 for v in vertices}

  def find(self, v):
    if self.parent[v] != v:
      self.parent[v] = self.find(self.parent[v])  # Path compression
    return self.parent[v]

  def union(self, u, v):
    rootU = self.find(u)
    rootV = self.find(v)
    if rootU != rootV:  # Only union if they are in different sets
      # Union by rank
      if self.rank[rootU] > self.rank[rootV]:
        self.parent[rootV] = rootU
      elif self.rank[rootU] < self.rank[rootV]:
        self.parent[rootU] = rootV
      else:
        self.parent[rootV] = rootU
        self.rank[rootU] += 1


def reverse_delete(graph):
  edges = [(u, v, graph.edge_weights[(u, v)]) for u, v in graph.edges]
  edges.sort(key=lambda x: x[2])  # Sort by weight in descending order
  # edges.sort(key=lambda x: x[2], reverse=True)


  uf = UnionFind(graph.vertices)
  mst = set(graph.edges)

  for u, v, w in edges:
    # Try removing the edge
    mst.remove((u, v))
    if uf.find(u) != uf.find(v):
      # If removing the edge does not disconnect the graph, skip re-adding it
      uf.union(u, v)
      mst.add((u, v, w))
      # print("skipped")
    # else:
    #     # If removing it disconnects the graph, add it back

    # print("gud")
  return mst
