def statement_generator(statement, decoration):
    print(f"{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Instructions", "-")

    print ('''
Instructions go here.
- instruction 1
- instruction 2
- etc
    ''')


want_instructions = input("Press <enter> to read instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()

print ("program continues")
