"""
File: nested_for_loop.py
Name: Alex
------------------------
This program shows students the basic
concepts of nested (double) for loop
by printing a 4-row-3-col rectangle
"""

# These constants control the diameter of the rectangle
ROW = 4  # The number of rows
COL = 3  # The number of cols


def main():
	for i in range(ROW):
		for j in range(COL):
			print('#', end="")
		print("")
"""
practice
###
###
###
"""


# def main():
#
# 	for i in range(3):
# 		for j in range(i+1):
# 			print('#', end="")
# 		print("")
"""
practice
#
##
###
"""


# def main():
# 	for i in range(3):
# 		for j in range(1, 4):
# 			print('#', end="")
# 		print("")
"""
practice
###
###
###
"""


# def main():
# 	for i in range(4):
# 		for j in range(4):
# 			if (i+j) % 2 == 0:
# 				print('#', end="")
# 			else:
# 				print(' ', end="")
# 		print('')
"""
practice
#　＃
　＃　＃
＃　＃
　＃　＃
"""


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
	main()
