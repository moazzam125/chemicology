'''
Database
--------
database for project operations.
'''

import os.path
import json

# Metadata

with open(os.path.dirname(__file__) + '/data/metadata.json', 'r') as metadata_file:
    metadata_content = json.load(metadata_file)

main_dict = metadata_content["main"]
main = {
    "name": main_dict["name"],
    "copyright_n": main_dict["copyright_n"],
    "discription": main_dict["discription"],
}

operation_dict = metadata_content["operations"]
operations = {
    "e": operation_dict["e"],
}

# Standards

std_dash = "------------------"

# Elements data

with open(os.path.dirname(__file__) + "/data/periodic_table.json", 'r') as pt_file:
    pt_content = json.load(pt_file)

def element(name, info_type):
    '''Datatsore of elements'''

    element_dict = pt_content[name]
    info_msg = element_dict[info_type]
    return info_msg

# Errors

error = {
    'g': "invalid operation!",
}