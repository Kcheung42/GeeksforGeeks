
def countSubsequence(a, sequence):
	if len(sequence) == 0:
		return 1
	if len(a) == 0:
		return 0
	result = 0
	result += countSubsequence(a[1:], sequence) #discard
	if a[0] == sequence[0]: #match
		result += countSubsequence(a, sequence[1:])
	return result

a = '312415926533'
print(countSubsequence(a, '123'))
