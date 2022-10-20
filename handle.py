import pygame
from time import sleep

x_index = 50
y_index = 50

def read_file(file_name):
	f=open(file_name,'r')
	n_bonus_points = int(next(f)[:-1])
	bonus_points = []
	for i in range(n_bonus_points):
		x, y, reward = map(int, next(f)[:-1].split(' '))
		bonus_points.append((x, y, reward))

	text=f.read()
	matrix=[list(i) for i in text.splitlines()]
	f.close()
	return bonus_points, matrix

def matrix_hoa(matrix):
	l = []
	t = []
	i = 0
	dong = len(matrix)
	cot = len(matrix[0])
	while i < dong:
		j = 0
		while j < cot:
			if( matrix[i][j] != 'x'):
				l.append([[i,j]])
			if(matrix[i][j] == 't'):
				t.append([[i,j]])
			# if matrix[i][j] == '':
			j+=1
		i+=1
	print(t)
	for x in l:
		if t != []:
			if x == t[0]:
				x1 = t[1][0][0] + 1
				y1 = t[1][0][1] + 1
				x_1 = t[1][0][0] - 1
				y_1 = t[1][0][1] - 1
			elif x == t[1]:
				x1 = t[0][0][0] + 1
				y1 = t[0][0][1] + 1
				x_1 = t[0][0][0] - 1
				y_1 = t[0][0][1] - 1
		else:	
			x1 = x[0][0] + 1
			y1 = x[0][1] + 1
			x_1 = x[0][0] - 1
			y_1 = x[0][1] - 1
		if y1 < cot and matrix[x1 - 1][y1] != 'x':
			x.append( [ x1 - 1, y1 ] )

		if x1 < dong and matrix[x1][y1 - 1] != 'x':
			x.append([x1, y1-1])

		if x_1 >= 0 and (matrix[x_1][y1 - 1] != 'x'):
			x.append([x_1, y1 - 1])

		if y_1 >= 0 and (matrix[x1 - 1][y_1] != 'x'):
			x.append([x1 - 1, y_1])
		
		if x1 - 1 == 0 or x1 - 1 == dong - 1 or y1 - 1 == 0 or y1 - 1 == cot - 1:
			end = x[0]
		if matrix[x[0][0]][x[0][1]] == 'S':
			start = x[0]
	return l, start, end

def test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay):     
	""" pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Hello world!')
	DISPLAYSURF.fill((255, 255, 255)) """

	""" Draw map """
	tele_index = []
	i = 0
	for x in matrix:
		j = 0
		for y in x:
			if y == 'x':
				pygame.draw.rect(DISPLAYSURF, (94, 88, 115), (j*x_index, i*y_index, x_index, y_index),0,round(x_index/5))
				pygame.draw.rect(DISPLAYSURF, (75, 70, 92), (j*x_index, i*y_index, x_index, y_index),round(x_index/6), round(x_index/6))
				pygame.display.update()
			if y == '+':
				xanh = (0 , 255 , 0)
				font = pygame.font.Font('freesansbold.ttf', x_index)
				text_bonus= font.render('+', True, xanh)
				DISPLAYSURF.blit(text_bonus, (j*x_index + round(x_index/10), i*y_index - round(y_index/20)))
				pygame.display.update()
			if y == 't':
				tele_index.append([i,j])
				pygame.draw.rect(DISPLAYSURF, (239, 54, 189), (j*x_index + (x_index/20), i*y_index + (x_index/20), x_index - round(x_index/10), y_index - round(x_index/10)),0,round(x_index/10))
				pygame.display.update()
			# if y == 'S':
			#     pygame.draw.rect(DISPLAYSURF, (249, 244, 0), (j*x_index, i*y_index, x_index, y_index))
			#     pygame.display.update()
			j += 1
		i += 1
	""" end draw map """
	print(tele_index)
	# ve diem ket thuc
	font = pygame.font.Font('freesansbold.ttf', round(x_index/3))
	text_End = font.render('EXIT', True, (255, 0, 0))
	DISPLAYSURF.blit(text_End, (end[1]*x_index + round(x_index/10), end[0]*y_index + round(y_index/3)))

	# ve diem bắt đầu
	vang = (238 , 210 , 2)
	font = pygame.font.Font('freesansbold.ttf', x_index + round(x_index/4))
	text_start= font.render('*', True, vang)
	DISPLAYSURF.blit(text_start, (start[1]*x_index + round(x_index/4), start[0]*y_index + round(y_index/4)))
	# pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (j*x_index, i*y_index, x_index, y_index))
	pygame.display.update()
	# 
	for i in route2:
		DISPLAYSURF.blit(text_End, (end[1]*x_index + round(x_index/10), end[0]*y_index + round(y_index/3)))
		DISPLAYSURF.blit(text_start, (start[1]*x_index + round(x_index/4), start[0]*y_index + round(y_index/4)))
		if i not in tele_index:
			pygame.draw.rect(DISPLAYSURF, (65, 171, 176), (i[1]*x_index + (x_index/20), i[0]*y_index + (x_index/20), x_index - round(x_index/10), y_index - round(x_index/10)),0,round(x_index/10))
			pygame.display.update()
		sleep(delay)
	
	

	for i in route:
		DISPLAYSURF.blit(text_End, (end[1]*x_index + round(x_index/10), end[0]*y_index + round(y_index/3)))
		if i not in tele_index:
			pygame.draw.rect(DISPLAYSURF, (226, 85, 93), (i[1]*x_index + (x_index/20), i[0]*y_index + (x_index/20), x_index - round(x_index/10), y_index - round(x_index/10)),0,5)

		DISPLAYSURF.blit(text_start, (start[1]*x_index + round(x_index/4), start[0]*y_index + round(y_index/4)))
		pygame.display.update()
    
"""     while True:
	for event in pygame.event.get():
	    if event.type == QUIT:
	        pygame.quit()
	        sys.exit() """

class Node:
	def __init__(self, coordinates, par = None, cost = 1):
		self.coordinates = coordinates
		self.par = par
		self.cost = 1

def main_route(O, mainroute):
	mainroute.append(O.coordinates)
	if O.par != None:
		main_route(O.par, mainroute)
	else:
		return



