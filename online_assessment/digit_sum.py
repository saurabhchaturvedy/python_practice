def digit_sum(n: int) -> int:
    """Compute the sum of digits of a number."""
    return sum(map(int, str(n)))

def evolve(n: int) -> int:
    """Generate the next number in the transformation chain."""
    return n + digit_sum(n)

def converge_sequences(seed1: int, seed2: int) -> int:
    """
    Evolve both sequences starting from `seed1` and `seed2`,
    by repeatedly updating the smaller one until both match.
    """
    while seed1 != seed2:
        if seed1 < seed2:
            seed1 = evolve(seed1)
        else:
            seed2 = evolve(seed2)
    return seed1

# Demo Execution
if __name__ == "__main__":
    initial_1, initial_2 = 471, 480
    meeting_value = converge_sequences(initial_1, initial_2)
    print(f"Converging point for {initial_1} and {initial_2} is {meeting_value}")
