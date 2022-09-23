#!/usr/bin/env python3

import algo as algo

class command:
    run = True
    first = False
    size = 0
    matrice = []

    info_dict = {
        "timeout_turn": 0,
        "timeoout_match": 0,
        "max_memory": 0,
        "time_left": 0,
        "game_type": 0,
        "rule": 0,
        "evaluate": [0, 0],
        "folder": ""
    }

    def start(size):
        if size < 5:
            print("ERROR message")
        else:
            command.size = size
            command.matrice = [[0 for x in range(command.size)] for y in range(command.size)]
            print("OK")

    def begin():
        command.first = True
        x, y = algo.lunch(command.first, command.size, command.matrice, 0, 0, command.info_dict, True)
        command.matrice[y][x] = 1
        print("%.0f,%.0f" % (x, y))

    def info(key, value):
        command.info_dict[key] = value
        return

    def board():
        while True:
            line = input()
            if line == "DONE":
                x, y = algo.lunch(command.first, command.size, command.matrice, 0, 0, command.info_dict, True)
                command.matrice[y][x] = 1
                print("%i,%i" % (x, y))
                return
            else:
                commandline = line.strip().split(",")
                command.matrice[int(commandline[1])][int(commandline[0])] = int(commandline[2])

    def turn(x, y):
        command.matrice[y][x] = 2
        x, y = algo.lunch(command.first, command.size, command.matrice, x, y, command.info_dict)
        command.matrice[y][x] = 1
        print("%i,%i" % (x, y))

    def end():
        command.run = False
        return

    def about():
        print('name="Gomoku", version="1.0", author="Pierre, Paul, Adrien", country="France"')

    def unknown():
        print("UNKNOWN")

def parse(cmd, args):
    if cmd == "START": command.start(int(args[0]))
    elif cmd == "BEGIN": command.begin()
    elif cmd == "INFO": command.info(args[0], args[1])
    elif cmd == "BOARD": command.board()
    elif cmd == "TURN": command.turn(int(args[0].split(",")[0]), int(args[0].split(",")[1]))
    elif cmd == "ABOUT": command.about()
    elif cmd == "END": command.end()
    else: command.unknown()

def main():
    while command.run:
        line = input()
        commandline = line.strip().split(" ")
        parse(commandline[0], commandline[1:])
    exit(0)

main()