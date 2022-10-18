import pygame, sys
import bfs, dfs, UCS_Test, GBFS_test, Astar_test
import handle
from pygame.locals import *

def main():
    pygame.init()
    pygame.display.set_caption('Hello world!')
    bonus_points, matrix = handle.read_file('maze_map (1).txt')
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
    DISPLAYSURF.fill((229, 191, 135))
    visited = [[False for i in range(col)] for j in range(row)]
    route = []
    route2 = []
    #dfs.dfs(l, bonus_points, start, end, visited, route, route2)
    #bfs.bfs(l, bonus_points, start, end, visited, route, route2)
    UCS_Test.ucs(l, bonus_points, start, end, visited, route, route2)

    handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()