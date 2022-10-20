import pygame, sys
import handle, solve
import bfs, dfs, UCS_Test, GBFS_test, Astar_test
from pygame.locals import *

def main(input):
    pygame.init()
    pygame.display.set_caption('Hello world!')
    solve.solve(input)
    
    #dfs.dfs(l, bonus_points, start, end, visited, route, route2)
    #UCS_Test.ucs(l, bonus_points, start, end, visited, route, route2)
    #handle.test_init(matrix, bonus_points, route2, route, DISPLAYSURF, end, start, delay)
    #pygame.image.save(DISPLAYSURF, "screenshot.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
               	pygame.quit()
                sys.exit()

if __name__ == "__main__":
    globals()["main"](sys.argv[1])
