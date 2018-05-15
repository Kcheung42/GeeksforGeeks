# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    M_Coloring_Problem.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kcheung <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/26 15:20:28 by kcheung           #+#    #+#              #
#    Updated: 2018/03/26 15:22:36 by kcheung          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.graph = [ [ 0 for col in range(vertices) ] for row in range(vertices) ]

g  = Graph(4)
g.graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
print(g.graph)
m=3

