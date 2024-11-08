def int_check(question, low):
    error = "Invalid value\n"
    while True:

        try:
            response = int(input(question))
            if response >= low:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


def integer_calc():
    integer = int_check("Integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(raw_binary)

    answer = f"{integer} in binary is {binary}. {num_bits} can represent it"

    return answer


print_integer = integer_calc()
print(print_integer)

