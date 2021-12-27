'''
Metadata
--------
extract and express information
'''

from database import main, operations, std_dash

def show_main():
        main_msg = main["name"] + "\n"+ std_dash + "\n" + main["copyright_n"] + "\n" + main["discription"]
        return main_msg

def show_ops():
    return '\n'.join([f'{key} = {val}' for key, val in operations.items()])