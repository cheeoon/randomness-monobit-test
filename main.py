import random


def generate_bit_stream(length):
    return [random.randint(0, 1) for _ in range(length)]


def monobit_test(bit_stream):
    ones_count = sum(bit_stream)
    return 9725 <= ones_count <= 10275


# Generate and test bit streams until a valid one is found
bit_stream = generate_bit_stream(20000)
while not monobit_test(bit_stream):
    bit_stream = generate_bit_stream(20000)
# Count the number of 1s and 0s in the valid bit stream
ones_count = sum(bit_stream)
zeros_count = len(bit_stream) - ones_count

bit_stream, ones_count, zeros_count
