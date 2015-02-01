import sys
import random

#inp = sys.stdin             #use this for the actual submission codes
#inp = open(filename, 'r')  #use this for testing locally
try:
	inp = sys.argv[1]
except IndexError:
	inp = ','

my_move, opp_move = inp.split(',')[0], inp.split(',')[1]

print(random.choice(['B', 'P', 'S']))