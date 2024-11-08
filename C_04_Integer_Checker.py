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


for item in range(0, 2):
    integer = int_check("Integer: ", 0)
    print(integer)

print()

for item in range(0, 2):
    height = int_check("Height: ", 1)
    print(height)