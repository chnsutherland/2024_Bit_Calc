def get_filetype():
    response = input("File type: ").lower()

    while True:
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


while True:
    file_type = get_filetype()

    if file_type == 'i':
        want_image = input("Please <enter> for an integer or any other key for image. ")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break
