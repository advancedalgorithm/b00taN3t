import os

def start_panel():
    while True:
        data = input("root@b00tanet ~ # ")

        if len(data) < 2:
            continue;

        if data == "help":
            print("Works")