# It seems like any non null natural number as a multiple that is composed only of one and zero
# http://math.stackexchange.com/questions/83932/a-natural-number-multiplied-by-some-integer-results-in-a-number-with-only-ones-a
# by multiplying this number by 2,3,..,9, you prove that Beatrix Trotter 
# will always fall asleep if N != 0

# So we can just naively browse the multiples of N
# and check the digits that compose them
# until we have seen the ten digits

for i in range(int(input())):
	N = int(input())

	if N == 0:
		print("Case #{}: {}".format(i+1, 'INSOMNIA'))
	else:
		seen = [False] * 10
		seenNb = 0
		multiple = 0
		while seenNb != 10:
			multiple += 1
			s = str(multiple*N)
			for c in s:
				digit = ord(c) - 48
				if seen[digit] == False:
					seen[digit] = True
					seenNb += 1
		print("Case #{}: {}".format(i+1, multiple*N))
