import sys

MAX_INPUT_SIZE = 100

def modify_num(input_num, threshold, limit, sum):
    # Apply threshold
    input_num = max(0, input_num - threshold)

    # Apply limit
    if input_num + sum > limit:
        input_num = max(0, limit - sum)

    return input_num

def compute(threshold, limit):
    sum = 0.0

    input_nums = []
    for _ in range(MAX_INPUT_SIZE):
        try:
            input_nums.append(float(input()))
        except EOFError:
            break

    for input_num in input_nums:
        modified_num = modify_num(input_num, threshold, limit, sum)
        print(modified_num)
        sum += modified_num

    print(sum)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Expected input is two command-line arguments: `threshold` and `limit`")
    else:
        compute(float(sys.argv[1]), float(sys.argv[2]))
