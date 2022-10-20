import handle
import math
   
def gbfs(matrix, bonus_points, Start, End, visited, route, route_gbfs):
    # distance_start = (Start[0] - End[0]) ** 2 + (Start[1] - End[1]) ** 2
    start = handle.Node(Start)
    open = []
    open.append(start)
    route_gbfs.append(Start)
    visited[start.coordinates[0]][start.coordinates[1]] = True
    while True:
        """ tim kiem that bai """
        if len(open) == 0:
            print('tim kiem that bai')
            route.clear()
            return

        """ danh dau da qua """

        #open.sort(key= lambda x: x.cost, reverse = True)
        O = open.pop(-1)
        # route_astar.append(O.coordinates)


        """ tim kiem thanh cong """
        if O.coordinates[0] == End[0] and O.coordinates[1] == End[1]:
            print('tim kiem thanh cong')
            print(O.coordinates)
            handle.main_route(O, route)
            return O
        
        """ Tim vitri O trong matrix """
        index = 0
        for i in matrix:
            if i[0] == O.coordinates:
                index = matrix.index(i)

        stack = []
        for i in matrix[index]:
            cost = math.sqrt(abs(i[0] - End[0]) + abs(i[1] - End[1]))
            tmp = handle.Node(i, None, cost)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                stack.append(tmp)
                route_gbfs.append(tmp.coordinates)
                visited[i[0]][i[1]] = True
        stack.sort(key = lambda x: x.cost, reverse= True)
        open = open + stack
        print(open[0].coordinates)
