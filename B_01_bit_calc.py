def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")

    print('''
Instructions go here.
- instruction 1
- instruction 2
- etc
    ''')


def get_filetype():
    while True:

        response = input("File type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"

        elif response in ['image', 'img']:
            return "image"

        elif response in ['text', 'txt']:
            return "text"

        else:
            print("Please enter a valid file type")


def calc_text_bits():
    pass

    response = input("Enter some text: ")

    num_chars = len(response)
    num_bits = num_chars * 8

    answer = f"{response} has {num_chars} characters. We need {num_chars} * 8 bits to represent it which is {num_bits} bits"

    return answer

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


def image_calc():
    width = int_check("Width: ", 1)
    height = int_check("Height: ", 1)

    num_pixels = width * height
    num_bits = num_pixels * 24

    answer = f"Number of pixels:  {width} * {height} = {num_pixels} \nNumber of bits: {num_pixels} * 24 = {num_bits}"

    return answer


def integer_calc():
    integer = int_check("Integer: ", 0)

    raw_binary = bin(integer)

    binary = raw_binary[2:]
    num_bits = len(raw_binary)

    answer = f"{integer} in binary is {binary}. {num_bits} can represent it"

    return answer


want_instructions = input("Press <enter> to read instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()

while True:
    file_type = get_filetype()

    if file_type == "xxx":
        break

    if file_type == 'i':
        want_image = input("Please <enter> for an integer or any other key for image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    if file_type == "image" 
        image_ans = image_calc()
        print(image_ans)
    elif file_type == "integer":
        integer_ans = integer_calc()
        print(integer_ans)
    else:
        text_ans = calc_text_bits()
        print(text_ans)
