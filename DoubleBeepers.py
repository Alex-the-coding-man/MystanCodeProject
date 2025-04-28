"""
File: DoubleBeepers.py
Name:Alex
-------------------------------
This program double the beepers on the map.
"""

from karel.stanfordkarel import *


def main():
    move()
    double()
    put_beepers_back()


def double():
    pick_one_put_two()
    move_back()


def put_beepers_back():
    while not facing_west():
        turn_left()
    while front_is_clear():
        move()
    turn_around()


def move_back():
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()


def pick_one_put_two():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()


def turn_around():
    turn_left()
    turn_left()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
