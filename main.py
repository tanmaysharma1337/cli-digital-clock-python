from draw_digits import draw_digits
from time import sleep,strftime
from os import system
import json

with open ("config.json","r") as f:
    CONFIG = json.loads(f.read())
    f.close()

dig_gap = CONFIG["dig_gap"]
y_len = CONFIG["y_len"]
update_interval = CONFIG["update_interval"]

def draw_time_now():
    draw_digits(strftime("%H:%M:%S"),y_len,dig_gap)

while True:
    system("cls")
    draw_time_now()
    sleep(update_interval)
