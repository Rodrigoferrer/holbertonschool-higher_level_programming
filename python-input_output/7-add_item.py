#!/usr/bin/python3
"""Python3"""


save_to_json_file = __import__("save_to_json_file").save_to_json_file
load_from_json_file = __import__("load_from_json_file").load_from_json_file


filename = "add_item.json"

try:
    items = load_from_json_file(filename)

except FileNotFoundError:
    items = list

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
