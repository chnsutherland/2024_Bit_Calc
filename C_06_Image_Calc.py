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


image_ans = image_calc()
print(image_ans)
