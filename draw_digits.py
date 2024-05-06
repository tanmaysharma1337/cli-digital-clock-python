from integer_array import character_array
import json

with open ("config.json","r") as f:
    CONFIG = json.loads(f.read())
    f.close()

def draw_digits(print_string,y_len,dig_gap):
    for i in range(y_len):
        set_row = ""
        for char in print_string:
            set_row += character_array()[char][i] + " "*dig_gap
        print(set_row)