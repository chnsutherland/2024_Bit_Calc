def get_filetype():
    while True:

        response = input("File type: ").lower()

        if response == "xxx" or response == "i":
            return response

        elif response in ['integer', 'int']:
            return "integer"

        elif response in ['image', 'img', 'picture', 'p']:
            return "image"

        elif response in ['text', 'txt', 't']:
            return "text"

        else:
            print("Please enter a valid file type")


# main routine

while True:
    file_type = get_filetype()
    print(f"You chose {file_type}")

    if file_type == "xxx":
        break

print("we are done.")
