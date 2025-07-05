 Question: Find Terminal Node or Detect Cycle in Directed Path
You are given:

A start_node_id (could be an integer or a string).

Two lists: from_ids and to_ids, representing directed edges in a graph. Each index i in these lists defines an edge from from_ids[i] → to_ids[i].

The graph is a set of nodes with at most one outgoing edge per node, forming a chain-like structure (or multiple chains).

Your task:
Write a function compute(start_node_id, from_ids, to_ids) that:

Follows the directed edges starting from start_node_id.

At each step, go to the node that the current node points to.

If you reach a node that has no outgoing edge, return that node.

If you detect a cycle, return the node that you visited just before stepping into a repeated node (i.e., just before revisiting any already-visited node).

