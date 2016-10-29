import math

def partitions(n,k,l=1):
	if k < 1:
		raise StopIteration
	if k == 1:
		if n < 7:
			if n >= l:
				yield (n,)
			raise StopIteration
	for i in range(l,n+1):
		for result in partitions(n-i,k-1,i):
			yield (i,)+result

def combination(n):
	d = dict()
	for item in n:
		if d.has_key(item):
			d[item] = d[item] + 1
		else:
			d[item] = 1
	div = 1
	for key, value in d.iteritems():
		div = div * math.factorial(value)

	return math.factorial(len(n))/div

def main():
	N = 8
	M = 24
	pairs = list()
	s = 0
	length = 0
	mult = list()
	for item in partitions(M,N):
		multiplication = 1
		for i in item:
			multiplication = multiplication*i
		mult.append(multiplication)
		
		for i in range(combination(item)):
			s = s + multiplication
			pairs.append(item)
			length = length+1

	mean = float(s)/length
	print mean
	#print pairs
	s = 0
	for x in mult:
		s = s + (x - mean)*(x - mean)
	s = s/length
	s = math.sqrt(s)
	print s

if __name__ == '__main__':
	main()