# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03.Longest_Increasing_Subsequence.py               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <kcheung@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/12/21 11:02:16 by kcheung           #+#    #+#              #
#    Updated: 2018/03/13 16:48:59 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def LIS(arr):
	n = len(arr)
	lis = [1]*n
	for i in range(1, n):
		for j in range(0, i):
			if arr[j] < arr[i] and lis[i] < lis[j] + 1:
				lis[i] = lis[j] + 1
			print(lis)
	maximum = max(lis)
	# print(lis)
	return maximum

# Driver program to test above function
# arr = [10, 22, 9, 33, 21, 50, 41, 60]
arr = [1,2,3,2,1,4,1,6,8,10]
print ("Length of lis is", LIS(arr))
