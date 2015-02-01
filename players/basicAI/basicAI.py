import sys
import functools

#inp = sys.stdin.read()

#my_move, opp_move = inp.split(',')[0], inp.split(',')[1]

my_move = 'PPPSSSPPPPPSSP' #expected 1
opp_move = 'PSSPS' #expected 2

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

current_sharp = get_sharpness(my_move)

print(current_sharp)