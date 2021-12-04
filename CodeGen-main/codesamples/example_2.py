def main(n):
    if n in {0, 1}:  # Base case
        return n
    return main(n - 1) + main(n - 2)  # Recursive case