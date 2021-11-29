def reverse_string(user_input):
    some_string = str(user_input)
    reversed_string = ""
    for current_index in range(len(some_string) - 1, -1, -1):
        reversed_string += some_string[current_index]

    return reversed_string


if __name__ == '__main__':
    # Example provided in the challenge
    user_input = 127
    reversed_string = reverse_string(user_input)
    print(reversed_string)
