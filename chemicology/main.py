'''
Main
----
initialize the program
'''

import metadata, operations
from database import error, std_dash

print(metadata.show_main())

while True:

    command = input("command: ")

    if command == 'p':
        print(metadata.show_ops())
    if command == 'e':
        print("Empirical Formula\n-----------------")
        print("Provide information:")
        e_C_per = input("C = ")
        e_H_per = input("H = ")
        e_O_per = input("O = ")

        operation = operations.Empirical_foumula(e_C_per, e_H_per, e_O_per)
        operation.gram_atoms()
        op_output = operation.atomic_ratio()
        print(std_dash + "\nRatio: " + str(op_output[0]) + " : " + str(op_output[1]) + " : " + str(op_output[2])+ "\n" + std_dash)

        command = input("show method(y/n): ")
        if command == 'y':
            print(std_dash + "\n" + operation.show_method() + "\n" + std_dash)

    elif command == 'q':
        break
    else:
        print(error["g"])