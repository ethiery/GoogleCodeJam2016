#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Code Jam 2016
# Round 1A
# Exercise 1
#
# @author Etienne THIERY

for i in range(int(input())):
	s = input()
	res = []
	for c in s:
		if len(res) == 0 or c >= res[0]:
			res = [c] + res
		else:
			res.append(c)
	print('Case #{}: {}'.format(i+1, ''.join(res)))
