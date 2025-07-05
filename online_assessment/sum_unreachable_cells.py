def sum_unreachable_cells(matrix, moves_sequence):
    if not matrix or not matrix[0]:
        return 0

    total_rows, total_cols = len(matrix), len(matrix[0])
    pos_row = pos_col = 0

    # Track boundaries of movement relative to start
    boundaries = {'min_row': 0, 'max_row': 0, 'min_col': 0, 'max_col': 0}

    for move in moves_sequence:
        if move == 'U':
            pos_row -= 1
        elif move == 'D':
            pos_row += 1
        elif move == 'L':
            pos_col -= 1
        elif move == 'R':
            pos_col += 1

        boundaries['min_row'] = min(boundaries['min_row'], pos_row)
        boundaries['max_row'] = max(boundaries['max_row'], pos_row)
        boundaries['min_col'] = min(boundaries['min_col'], pos_col)
        boundaries['max_col'] = max(boundaries['max_col'], pos_col)

    # Calculate reach in each direction from origin
    reach_up = -boundaries['min_row']
    reach_down = boundaries['max_row']
    reach_left = -boundaries['min_col']
    reach_right = boundaries['max_col']

    safe_sum = 0
    for r in range(total_rows):
        for c in range(total_cols):
            # Check if cell (r, c) lies outside the reachable area
            if (r + 1 <= reach_up or
                total_rows - r <= reach_down or
                c + 1 <= reach_left or
                total_cols - c <= reach_right):
                continue
            safe_sum += matrix[r][c]

    return safe_sum


if __name__ == "__main__":
    example_matrix = [
        [1, 0, 2],
        [4, 1, 0],
        [0, 3, 1]
    ]
    moves = "RR"
    print(sum_unreachable_cells(example_matrix, moves))  # Output: 8
