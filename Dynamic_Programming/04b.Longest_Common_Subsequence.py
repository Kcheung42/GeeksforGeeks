# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04b.Longest_Common_Subsequence.py                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/21 12:45:34 by kcheung           #+#    #+#              #
#    Updated: 2017/12/21 12:45:35 by kcheung          ###   ########.fr        #
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

def LCS(str1, str2, m, n):
	if m == 0 or n == 0:
		return 0
	elif str1[m-1] == str2[n-1]:
		return 1 + LCS(str1, str2, m-2, n-2)
	else:
		return max(LCS(str1, str2, m-1, n), LCS(str1,str2, m, n-1))

'''
Time: O(2^n)
'''
