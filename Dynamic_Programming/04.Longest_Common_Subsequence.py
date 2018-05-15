# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04.Longest_Common_Subsequence.py                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/21 12:29:39 by kcheung           #+#    #+#              #
#    Updated: 2017/12/21 15:07:38 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''
Longest Repeated Subsequence
3.2
Given a string, print the longest repeating subseequence such that the two
subsequence don’t have same string character at same position, i.e., any i’th
character in the two subsequences shouldn’t have the same index in the original
string.

Example:
Input: str = "aabb"
Output: "ab"

Input: str = "aab"
Output: "a"
The two subssequence are 'a'(first) and 'a' 
(second). Note that 'b' cannot be considered 
as part of subsequence as it would be at same
index in both.
'''

def printLCS(L,m,n,str1):
	result = ''
	while(L[m][n] != 0):
		L[m][n] = L[m][n]
		if L[m-1][n] != L[m][n] and L[m][n-1] != L[m][n]:
			result += str1[m-1]
			m -= 1
			n -= 1
		elif L[m-1][n] == L[m][n]:
			m = m-1
		elif L[m][n-1] == L[m][n]:
			n = n-1
	print(" ".join(result[::-1]))

def LCS(str1, str2):
	m = len(str1)
	n = len(str2)
	L = [[0] * (n+1) for i in range(m+1)]
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 and j == 0:
				L[i][j] = 0
			elif str1[i-1] == str2[j-1]:
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	printLCS(L,m,n, str1)
	return L[m][n]

# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print(LCS(X,Y))

'''
Time: O(mn)
'''
