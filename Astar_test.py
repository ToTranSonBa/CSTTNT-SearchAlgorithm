from lib2to3.pgen2.token import EQUAL
from math import sqrt
from time import sleep
from turtle import distance
import pygame, sys
from pygame.locals import *



def read_file(file_name: str = 'maze.txt'):
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

def test_init(matrix, bonus_points, route2, route, DISPLAYSURF):     
    """ pygame.init()

    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hello world!')

    DISPLAYSURF.fill((255, 255, 255)) """

    """ Draw map """
    size1 = len(matrix[0])
    size2 = len(matrix)
    x_index = 800/22
    y_index = 600/11
    i = 0
    for x in matrix:
        j = 0
        for y in x:
            if y == 'x':
                pygame.draw.rect(DISPLAYSURF, (148, 83, 5), (j*x_index, i*y_index, x_index, y_index))
                pygame.display.update()
            if y == '+':
                pygame.draw.rect(DISPLAYSURF, (255, 0, 0), (j*x_index, i*y_index, x_index, y_index))
                pygame.display.update()
            if y == 'S':
                pygame.draw.rect(DISPLAYSURF, (249, 244, 0), (j*x_index, i*y_index, x_index, y_index))
                pygame.display.update()
            j += 1
        i += 1
    """ end draw map """
    for i in route2:
        pygame.draw.rect(DISPLAYSURF, (0, 150, 255), (i[1]*x_index, i[0]*y_index, x_index, y_index))
        pygame.display.update()
        sleep(0.1)
        pygame.draw.rect(DISPLAYSURF, (0, 255, 255), (i[1]*x_index, i[0]*y_index, x_index , y_index))
        pygame.display.update()

    for i in route:
        pygame.draw.rect(DISPLAYSURF, (0, 0, 255), (i[1]*x_index, i[0]*y_index, x_index , y_index))
        pygame.display.update()
    
"""     while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit() """

class Node:
    def __init__(self, coordinates, par = None, cost = 1, distance = 0):
        self.coordinates = coordinates
        self.par = par
        self.cost = cost
        self.distance = distance

def matrix_hoa(matrix):
  l = []
  i = 0
  dong = len(matrix)
  cot = len(matrix[0])
  while i < dong:
    j = 0
    while j < cot:
      if( matrix[i][j] != 'x'):
        l.append([[i,j]])
      j+=1
    i+=1

  for x in l:
    x1 = x[0][0] + 1
    y1 = x[0][1] + 1
    x_1 = x[0][0] - 1
    y_1 = x[0][1] - 1
    if y1 < cot and matrix[x[0][0]][y1] != 'x':
      x.append( [ x[0][0] , y1 ] )

    if x1 < dong and matrix[x1][x[0][1]] != 'x':
      x.append([x1, x[0][1]])

    if x_1 >= 0 and (matrix[x_1][x[0][1]] != 'x'):
      x.append([x_1, x[0][1]])

    if y_1 >= 0 and (matrix[x[0][0]][y_1] != 'x'):
      x.append([x[0][0], y_1])

    
    # if y1 < dong and x1 < cot and matrix[x1][y1] != 'x':
    #   x.append( [ x1 , y1 ] )

    # if y_1 >= 0 and x_1 >= 0 and matrix[x_1][y_1] != 'x':
    #   x.append([x1, y_1])

    # if x_1 >= 0 and y1 < dong and (matrix[x_1][y1] != 'x'):
    #   x.append([x_1, y1])

    # if y_1 >= 0 and x1 < cot and (matrix[x1][y_1] != 'x'):
    #   x.append([x1, y_1])
  return l

def main_route(O, mainroute = []):
    if O != None:
        mainroute.append(O.coordinates)
        print(O.coordinates)
        if O.par != None:
            main_route(O.par, mainroute)
        else:
            return
    
def bfs(matrix, bonus_points, Start, End, visited, route, route_bfs):
    start = Node(Start)
    open = []
    open.append(start)
    visited[start.coordinates[0]][start.coordinates[1]] = True
    while True:
        """ tim kiem that bai """
        if len(open) == 0:
            print('tim kiem that bai')
            route.clear()
            return

        """ danh dau da qua """
        O = open.pop(0)
        route_bfs.append(O.coordinates)
        """ tim kiem thanh cong """
        if O.coordinates[0] == End[0] and O.coordinates[1] == End[1]:
            print('tim kiem thanh cong')
            main_route(O, route)
            return O
        
        """ Tim vitri O trong matrix """
        index = 0
        for i in matrix:
            if i[0] == O.coordinates:
                index = matrix.index(i)

        for i in matrix[index]:
            tmp = Node(i)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                open.append(tmp)
                visited[i[0]][i[1]] = True


def Astar(matrix, bonus_points, Start, End, visited, route, route_astar):
    # distance_start = (Start[0] - End[0]) ** 2 + (Start[1] - End[1]) ** 2
    start = Node(Start)
    open = []
    open.append(start)
    route_astar.append(Start)
    visited[start.coordinates[0]][start.coordinates[1]] = True
    while True:
        """ tim kiem that bai """
        if len(open) == 0:
            print('tim kiem that bai')
            route.clear()
            return

        """ danh dau da qua """

        # open.sort(key= lambda x: x.cost)
        O = open.pop(-1)
        # route_astar.append(O.coordinates)


        """ tim kiem thanh cong """
        if O.coordinates[0] == End[0] and O.coordinates[1] == End[1]:
            print('tim kiem thanh cong')
            print(O.coordinates)
            main_route(O, route)
            return O
        
        """ Tim vitri O trong matrix """
        index = 0
        for i in matrix:
            if i[0] == O.coordinates:
                index = matrix.index(i)

        stack = []
        for i in matrix[index]:
            distance = (i[0] - End[0]) ** 2 + (i[1] - End[1]) ** 2 + O.cost + 1
            tmp = Node(i, None, O.cost + 1, distance)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                stack.append(tmp)
                route_astar.append(tmp.coordinates)
                visited[i[0]][i[1]] = True
        stack.sort(key = lambda x: x.distance, reverse= True)
        open = open + stack




def main():
    pygame.init()

    DISPLAYSURF = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Hello world!')

    DISPLAYSURF.fill((255, 255, 255))
    bonus_points, matrix = read_file('maze_map.txt')
    
    row = len(matrix)
    col = len(matrix[0])

    # test
    # matrix = [[" " for i in range(col)] for j in range(row)]
    # end test

    l = matrix_hoa(matrix)
    
    visited = [[False for i in range(col)] for j in range(row)]
    start = [8,15]
    end = [4, 0]
    route = []
    route2 = []
    # dfs(l, bonus_points, start, end, visited, route)
    Astar(l, bonus_points, start, end, visited, route, route2)
    print(route2)

    test_init(matrix, bonus_points, route2, route, DISPLAYSURF)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()




if __name__ == "__main__":
    main()