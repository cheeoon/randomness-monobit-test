import random


def generate_bit_stream(length):
    return [random.randint(0, 1) for _ in range(length)]


def number_of_ones_test(ones_count):
    return 9725 <= ones_count <= 10275


def monobit_test(ones_count, zeros_count):
    calculation = ((zeros_count - ones_count) ** 2) / (zeros_count + ones_count)
    return calculation


def main():
    thresold_value = 3.8415  # alpha=0.05 v=1
    loop_count = 0
    valid_stream = False

    while not valid_stream:
        # Generate and test bit streams until a valid one is found
        bit_stream = generate_bit_stream(20000)
        loop_count += 1
        ones_count = sum(bit_stream)
        zeros_count = len(bit_stream) - ones_count
        print(f"{loop_count} round bit stream generated")
        print(f"the generated bit stream is {''.join(str(x) for x in bit_stream)}")
        if ones_count + zeros_count == len(bit_stream):
            print("The bit stream counting is correct")
        else:
            print("The bit stream counting is NOT correct")

        if number_of_ones_test(ones_count):
            print(f"Passed number_of_ones_test. 1's:{ones_count}; 0's:{zeros_count}")
            monobit_value = monobit_test(ones_count, zeros_count)
            if monobit_value <= thresold_value:
                print(f"Passed monobit_test with value {monobit_value}")
                valid_stream = True
            else:
                print(
                    f"Failed monobit_test with value {monobit_value}, generating new bit stream"
                )
        else:
            print("Failed number_of_ones_test, generating new bit stream")


if __name__ == "__main__":
    main()
