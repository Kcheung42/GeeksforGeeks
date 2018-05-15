def fibRecur(n, lookup):
	if n == 0 or n == 1:
		lookup[n] = n
	if lookup[n] is None:
		lookup[n] = fibRecur(n-1, lookup) + fibRecur(n-2, lookup)
	return lookup[n]

def fib(n):
	lookup = [None] * (n+1)
	return (fibRecur(n, lookup))

def fib(n):
	f = [0] * (n+1)
	f[1] = 1
	for i in range(2, n+1):
		f[i] = f[i-1] + f[i-2]
	return f[n]

print(fib(100))

