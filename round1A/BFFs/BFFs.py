#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Code Jam 2016
# Round 1A
# Exercise 3
#
# @author Etienne THIERY

# This solution is valid but it is a little slow :
# it takes 3 minutes to solve the large input on an old laptop

def solve(kids, bffs, onlyPaths=False):
	N = len(kids)
	# the BFF of the last kid of a cycle is the first kid of this cycle
	# the BFF of the last kid of a path is the penultimate kid of this path
	cycles, paths = [], []
	# kids we haven't started a new path/cycle from
	starts = kids[:]
	while len(starts) > 0:
		new = [starts.pop(0)]
		# builds path, and enhances paths found previously if possible
		while bffs[new[-1]] not in new:
			enhanced_paths = []
			for p in paths:
				if bffs[new[-1]] == p[-1]:
					enhanced_p = p[:]
					for k in reversed(new):
						if k in enhanced_p:
							break
						else:
							enhanced_p.append(k)
					if len(enhanced_p) > len(p):
						enhanced_paths.append(enhanced_p)
			paths.extend(enhanced_paths)
			new.append(bffs[new[-1]])

		# Checks if the new path/cycle is a cycle, or a path
		begin = new.index(bffs[new[-1]])
		if begin != len(new)-2:
			new = new[begin:]
			cycles.append(new)
		else:
			paths.append(new)
		for k in new:
			if k in starts:
				starts.remove(k)

	cycles.append([])
	paths.append([])
	best_cycle = max(cycles, key=len)
	best_path = max(paths, key=len)
	# If the best solution found is a path, we can look
	# for another path to add to the solution among the
	# remaining kids
	if best_path != []:
		unreachable = best_path[:]
		i = 0
		while i < len(kids):
			if (kids[i] in unreachable) or (bffs[kids[i]] in unreachable):
				unreachable.append(kids.pop(i))
				i = 0
			else:
				i += 1
		best_path.extend(solve(kids, bffs, onlyPaths=True))

	if onlyPaths:
		return best_path
	else:
		return max([best_path, best_cycle], key=len)


for T in range(1, int(input())+1):
	N = int(input())
	bffs = [None] + [int(i) for i in input().split()]
	kids = [i+1 for i in range(N)]
	sol = solve(kids, bffs)
	print('Case #{}: {}'.format(T, len(sol)))
