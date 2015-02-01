"""
basicAI logic: it will sharpen on the first turn and then block
until the opponent reaches a dull stick.  Then it will poke.
If that fails, it will sharpen again and repeat.
"""

import sys
import functools

inp = sys.argv[1] if len(sys.argv) > 1 else ','
my_move, opp_move = inp.split(',')

#my_move = 'PPPSSSPPPPPSSPP' #expected 1
#opp_move = 'PSSPSPP' #expected 2

def get_sharpness(move_sequence: str):
	sharpness = 0
	for i in move_sequence:
		sharpness = change_in_sharp(sharpness, i)
	return sharpness


#
def change_in_sharp(current_sharp: int, action: str):
	if action == 'P' and current_sharp > 0:
		return current_sharp - 1
	elif action == 'S':
		return current_sharp + 1
	else:
		return current_sharp
#current_sharp = functools.reduce(change_in_sharp, my_move) #don't use reduce() in an example for beginners, it's more obscure to them.
#

if get_sharpness(opp_move) > 0:
	print('B')
else:
	if get_sharpness(my_move) == 0:
		print('S')
	else:
		print('P')
