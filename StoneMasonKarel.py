"""
File: StoneMasonKarel.py
Name: Alex
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition: Karel is on the first base, facing East
    post_condition: Karel is on the last base of pillar, facing East
    """
    for i in range(4):
        build_the_pillar()
        climb_down()
        if front_is_clear():
            for i in range(4):
                move()


def build_the_pillar():
    """
    pre-condition: Karel is on the base
    post_condition: Karel is on the top of the pillar
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
                put_beeper()
                move()
        else:
                move()
    if not on_beeper():
            put_beeper()
    turn_left()
    turn_left()


def climb_down():
    """
    pre-condition: Karel is on the top of the pillar
    post_condition: Karel is on the base of the pillar
    """
    while front_is_clear():
        move()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
