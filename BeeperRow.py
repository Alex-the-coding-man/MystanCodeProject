"""
File: BeeperRow.py
Name:Alex
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *



def main():
    """
    Karel will fill the first Street in any world
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
