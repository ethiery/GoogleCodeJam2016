# In the end, the number of operations needed
# is just the number of change of "same side up adjacent pancakes" groups 
# in the stack,
# + 1 if the pancake at the bottom of the stack is blank side up.
#
# e.g. : in --+---+-, there are 5 groups, and the bottom pancake is blank
# side up, so we would need at least 6 maneuvers
# --+---+-
# +++---+-
# ------+-
# +++++++-
# --------
# ++++++++

def solve(string):
	index = len(string)-1
	nbFlips = 1 if (current == '-') else 0
	current = string[index]
	while index >= 0:
		if string[index] != current:
			nbFlips += 1
			current = string[index]
		index -= 1
	return nbFlips 
		
nbCases = int(input())

for i in range(nbCases):
	solution = solve(input())
	print("Case #{}: {}".format(i+1, solution))