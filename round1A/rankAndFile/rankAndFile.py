#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Code Jam 2016
# Round 1A
# Exercise 2
#
# @author Etienne THIERY

def isValid(l, i, dim, otherDim):
	for j, l2 in otherDim.items():
		if l[j] != l2[i]:
			return False
	for j, l2 in dim.items():
		if j < i:
			for k in range(len(l)):
				if int(l[k]) <= int(l2[k]):
					return False
	return True

def solution_knowing(N, lists, rows, cols):
	# terminal case of the recursion
	if len(lists) == 0:
		return rows, cols
	else:
		found_obvious = True
		while found_obvious:
			found_obvious = False
			possibilities = {}
			# Computes the differents rows and columns each list could be
			for l in lists:
				possibilities[tuple(l)] = []
				for i in range(N):
					for dim1, dim2 in [(rows, cols), (cols,  rows)]:
						if (i not in dim1) and isValid(l, i, dim1, dim2):
								possibilities[tuple(l)].append((dim1, i))
				# If the list can't be any column or row, there is no solution
				if len(possibilities[tuple(l)]) == 0:
					return None
			# Sets all the columns or rows that are 100% sure
			for l, choices in possibilities.items():	
				if len(choices) == 1:
					l = list(l)
					dim, j = choices[0]
					dim[j] = l
					lists.remove(l)
					found_obvious = True

		# If there are no more lists to "assign", the instance is solved
		if len(lists) == 0:
			return rows, cols
		else:
			# Else, we make a supposition on one of the list for which there 
			# are the least different choices possible
			chosen, choices = min(possibilities.items(), key=lambda x: len(x[1]))
			chosen = list(chosen)
			for dim, j in choices:
				rec_lists = lists[:]
				rec_lists.remove(chosen)
				dim2 = cols if dim is rows else rows
				rec_dim = dim.copy()
				rec_dim[j] = chosen
				sol = solution_knowing(N, rec_lists, rec_dim, dim2)
				# if there is a solution, the supposition was good
				if sol != None:
					return sol
			# if none of the suppositions were good, then there is no solution
			return None

for T in range(1, int(input())+1):
	N = int(input())
	lists = [input().split() for i in range(2*N-1)]
	lists.sort(key=lambda l: int(l[0]))
	rows, cols = None, None
	if lists[0][0] == lists[1][0]:
		rows = {0:lists.pop(0)}
		cols = {0:lists.pop(0)}
	else:
		lists.sort(key=lambda l: int(l[-1]))
		rows = {N-1:lists.pop(-1)}
		cols = {N-1:lists.pop(-1)}
	rows, cols = solution_knowing(N, lists, rows, cols)
	# Looks for the missing row/col
	smaller = min((rows, cols), key=len)
	bigger = max((rows, cols), key=len)
	for i in range(N):
		if i not in smaller:
			missing = []
			for j in range(N):
				missing.append(bigger[j][i])
			print('Case #{}: {}'.format(T, ' '.join(missing)))
