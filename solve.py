import handle
import bfs, dfs, UCS_Test, GBFS_test, Astar_test
import pygame
import copy
import glob, os

def solve(input):
	if input == "all":
		pathInput = 'Input/Level1'
		for pathfile in glob.glob(os.path.join(pathInput, '*.txt')):
			filename = os.path.splitext(os.path.basename(pathfile))[0]
			print(filename)
			pathOutput = os.path.join('Output', filename)
			os.makedirs(pathOutput)
			print(pathOutput)
			bonus_points, matrix = handle.read_file(pathfile)
			l, start, end = handle.matrix_hoa(matrix)
			row = len(matrix)
			col = len(matrix[0])
			x_size = handle.x_index*col
			y_size = handle.x_index*row
			while x_size > 1920 or y_size > 1080:
				handle.x_index -= 10
				handle.y_index -= 10
				x_size = handle.x_index*col
				y_size = handle.x_index*row

			# bfs
			totalcost = 0
			DISPLAYSURF = pygame.display.set_mode((x_size, y_size))
			DISPLAYSURF.fill((255, 255, 255))
			visited = [[False for i in range(col)] for j in range(row)]
			route = []
			route2 = []
			delay = 0
		    	#dfs.dfs(l, bonus_points, start, end, visited, route, route2)
			bfs.bfs(l, bonus_points, start, end, visited, route, route2)
			handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
			pygame.image.save(DISPLAYSURF, os.path.join(pathOutput,"bfs.jpg"))
			f = open(pathOutput + "/bfs.txt", "w+")
			string = ""
			for i in route:
				string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
				totalcost += 1
			f.write(string)
			f.write("\nchi phi: " + str(totalcost))
			f.close()
			# dfs
			totalcost = 0
			visited = [[False for i in range(col)] for j in range(row)]
			route = []
			route2 = []
			DISPLAYSURF.fill((255, 255, 255))
			dfs.dfs(l, bonus_points, start, end, visited, route, route2)
			handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
			pygame.image.save(DISPLAYSURF, os.path.join(pathOutput, "dfs.jpg"))
			f = open(pathOutput + "/dfs.txt", "w+")
			string = ""
			for i in route:
				string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
				totalcost += 1
			f.write(string)
			f.write("\nchi phi: " + str(totalcost))
			f.close()
			# ucs
			totalcost = 0
			visited = [[False for i in range(col)] for j in range(row)]
			route = []
			route2 = []
			DISPLAYSURF.fill((255, 255, 255))
			UCS_Test.ucs(l, bonus_points, start, end, visited, route, route2)
			handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
			pygame.image.save(DISPLAYSURF, os.path.join(pathOutput, "ucs.jpg"))
			f = open(pathOutput + "/ucs.txt", "w+")
			string = ""
			for i in route:
				string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
				totalcost += 1
			f.write(string)
			f.write("\nchi phi: " + str(totalcost))
			f.close()
			# GBFS
			totalcost = 0
			visited = [[False for i in range(col)] for j in range(row)]
			route = []
			route2 = []
			DISPLAYSURF.fill((255, 255, 255))
			GBFS_test.gbfs(l, bonus_points, start, end, visited, route, route2)
			handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
			pygame.image.save(DISPLAYSURF, os.path.join(pathOutput, "gbfs.jpg"))
			f = open(pathOutput + "/gbfs.txt", "w+")
			string = ""
			for i in route:
				string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
				totalcost += 1
			f.write(string)
			f.write("\nchi phi: " + str(totalcost))
			f.close()
			# astar
			totalcost = 0
			visited = [[False for i in range(col)] for j in range(row)]
			route = []
			route2 = []
			DISPLAYSURF.fill((255, 255, 255))
			Astar_test.Astar(l, bonus_points, start, end, visited, route, route2)
			handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
			pygame.image.save(DISPLAYSURF, os.path.join(pathOutput, "astar.jpg"))
			f = open(pathOutput + "/astar.txt", "w+")
			string = ""
			for i in route:
				string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
				totalcost += 1
			f.write(string)
			f.write("\nchi phi: " + str(totalcost))
			f.close()
	if input == "advance":
		pathInput = 'Input/advance'
		pathfile = os.path.join(pathInput, 'Input1.txt')
		print(pathfile)
		bonus_points, matrix = handle.read_file(pathfile)
		l, start, end = handle.matrix_hoa(matrix)
		row = len(matrix)
		col = len(matrix[0])
		x_size = handle.x_index*col
		y_size = handle.x_index*row
		while x_size > 1920 or y_size > 1080:
			handle.x_index -= 10
			handle.y_index -= 10
			x_size = handle.x_index*col
			y_size = handle.x_index*row
		DISPLAYSURF = pygame.display.set_mode((x_size, y_size))
		DISPLAYSURF.fill((255, 255, 255))
		visited = [[False for i in range(col)] for j in range(row)]
		route = []
		route2 = []
		delay = 0.03
		dfs.dfs(l, bonus_points, start, end, visited, route, route2)
		handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
	if input == "test":
		pathInput = 'Input/Level1'
		pathfile = os.path.join(pathInput, 'Input5.txt')
		print(pathfile)
		bonus_points, matrix = handle.read_file(pathfile)
		l, start, end = handle.matrix_hoa(matrix)
		row = len(matrix)
		col = len(matrix[0])
		x_size = handle.x_index*col
		y_size = handle.x_index*row
		while x_size > 1920 or y_size > 1080:
			handle.x_index -= 10
			handle.y_index -= 10
			x_size = handle.x_index*col
			y_size = handle.x_index*row
		DISPLAYSURF = pygame.display.set_mode((x_size, y_size))
		DISPLAYSURF.fill((255, 255, 255))
		totalcost = 0
		visited = [[False for i in range(col)] for j in range(row)]
		route = []
		route2 = []
		delay = 0.01
		# GBFS_test.gbfs(l, bonus_points, start, end, visited, route, route2)
		Astar_test.Astar(l, bonus_points, start, end, visited, route, route2)
		#dfs.dfs(l, bonus_points, start, end, visited, route, route2)
		#bfs.bfs(l, bonus_points, start, end, visited, route, route2)
		handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
		string = ""
		for i in route:
			string = string + '(' + str(i[0]) + ', ' + str(i[1]) + '), ' 
		print(route)
		print(string)
		print(totalcost)
