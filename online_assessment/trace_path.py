def trace_path(start, edges_from, edges_to):
    """
    Traverse a one-way node chain starting from `start`.
    - If a cycle is encountered, return the node right before the loop.
    - If it terminates naturally, return the final node.
    """
    # Create a mapping from each source node to its destination
    transition = dict(zip(edges_from, edges_to))
    
    traversed = set()
    pointer = start
    last_node = None

    while pointer in transition:
        if pointer in traversed:
            # Detected a revisit — return last valid node before re-entry
            return last_node
        traversed.add(pointer)
        last_node = pointer
        pointer = transition[pointer]
    
    # Dead-end encountered (no further edge)
    return pointer

# Demonstration
if __name__ == "__main__":
    src_nodes = [1, 7, 3, 4, 2, 6, 9]
    dst_nodes = [3, 3, 4, 6, 6, 9, 5]

    print(trace_path(2, src_nodes, dst_nodes))  # Expected: 5 (linear path)

    # Cycle scenario
    f = ['A', 'B', 'C']
    t = ['B', 'C', 'A']
    print(trace_path('A', f, t))  # Expected: 'C' (right before re-entering 'A')
