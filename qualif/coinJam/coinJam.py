#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Google Code Jam 2016
# Qualifications
# Exercise 3
#
# @author Etienne THIERY

# A solution is to generate all the binary strings of N characters
# starting with a 1 and ending by a 1, and to look for coinJam among them.

# Because there are many binary strings, you can toss a coinJam if it
# is hard to find divisors to prove that it is a coinJam

# This is the key to solve an instance fast : only check a few divisors,
# for example only the primesunder100, and give up if you did not find
# a divisor for each base among them.


primesunder100 = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def quick_divisor(n):
    '''
    If n has a divisor among the prime numbers, returns it.
    Else, returns None.
    '''
    for x in primesunder100:
        if n % x == 0:
            return x
    return None


for testCase in range(int(input())):
	N, J = input().split(' ')
	N, J = int(N), int(J)

	print("Case #{}:".format(testCase+1))

	coinjamFound = 0
	# Generates all the binary strings of N characters starting with 1 and
	# ending with 1 if needed but stops if enough coin jams have been found
	for count in range(2**(N-2)):
		binaryString = '1{}1'.format(format(count, '0{}b'.format(N-2)))

		divisors = []
		for base in range(2, 11):
			nb = int(binaryString, base)
			divisor = quick_divisor(nb)
			if divisor == None:
				break
			divisors.append(divisor)

		if len(divisors) == 9:
			coinjamFound += 1
			print("{} {}".format(binaryString, ' '.join(map(str, divisors))))

		if coinjamFound == J:
			break