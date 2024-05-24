from graph import *


def boruvka(inGraph):
	mst = []  # Initialize the minimum spanning tree (MST)

	# While there are more than one component in the graph
	while len(set(inGraph.parent.values())) > 1:
		# Initialize the cheapest edge dictionary for each component
		cheapest_edge = {}

		# Iterate through each edge in the graph
		for edge in inGraph.edges:
			u, v = edge
			u_root = inGraph.find_set_boruvka(u)
			v_root = inGraph.find_set_boruvka(v)

			# If the endpoints of the edge belong to different components
			if u_root != v_root:
				# Check if this edge is the cheapest for its components
				if u_root not in cheapest_edge or (
				    inGraph.edge_weights[edge]
				    < inGraph.edge_weights[cheapest_edge[u_root]]):
					cheapest_edge[u_root] = edge
				if v_root not in cheapest_edge or (
				    inGraph.edge_weights[edge]
				    < inGraph.edge_weights[cheapest_edge[v_root]]):
					cheapest_edge[v_root] = edge

		# Add the cheapest edges to the MST
		for root, edge in cheapest_edge.items():
			u, v = edge
			if inGraph.find_set_boruvka(u) != inGraph.find_set_boruvka(
			    v):  # Check for cycle
				mst.append((u, v, inGraph.edge_weights[edge]))
				inGraph.union(u, v)

	return mst
