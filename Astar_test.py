# from random import random
# import handle
# import math

# def Astar(matrix, bonus_points, Start, End, visited, route, route_astar):
#     # distance_start = (Start[0] - End[0]) ** 2 + (Start[1] - End[1]) ** 2
#     start = handle.Node(Start)
#     open = []
#     open.append(start)
#     route_astar.append(Start)
#     visited[start.coordinates[0]][start.coordinates[1]] = True
#     while True:
#         """ tim kiem that bai """
#         if len(open) == 0:
#             print('tim kiem that bai')
#             route.clear()
#             return

#         """ lay phan tu dau theo cua open """

#         open.sort(key= lambda x: x.distance, reverse= True)
#         O = open.pop(-1)
#         # route_astar.append(O.coordinates)


#         """ tim kiem thanh cong """
#         if O.coordinates[0] == End[0] and O.coordinates[1] == End[1]:
#             print('tim kiem thanh cong')
#             print(O.coordinates)
#             handle.main_route(O, route)
#             return O
        
#         """ Tim vitri O trong matrix """
#         index = 0
#         for i in matrix:
#             if i[0] == O.coordinates:
#                 index = matrix.index(i)

#         # stack = []
#         for i in matrix[index]:
#             distance = math.sqrt((i[0] - End[0]) ** 2 + (i[1] - End[1]) ** 2) + O.cost + 1
#             # distance = math.sqrt(abs(i[0] - End[0]) + abs(i[1] - End[1])) + O.cost + 1
#             tmp = handle.Node(i, None, O.cost + 1, distance)
#             tmp.par = O
#             if visited[i[0]][i[1]] == False:
#                 open.append(tmp)
#                 route_astar.append(tmp.coordinates)
#                 visited[i[0]][i[1]] = True
#         # stack.sort(key = lambda x: x.distance, reverse= True)
#         # open = open + stack



import handle
import math

def equal_coordinates(O, bonus_points):
    if O[0] == bonus_points[0] and O[1] == bonus_points[1]:
        return 1
    else: 
        return 0


def Astar(matrix, bonus_points, Start, End, visited, route, route_astar):
    start = handle.Node(Start)
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
        open.sort(key= lambda x: x.distance, reverse= True)
        O = open.pop(-1)
        # route_astar.append(O.coordinates)

        # # xu ly bonus
        # for i in bonus_points:
        #     if equal_coordinates(O.coordinates, i) == 1:
        #         O.cost += i[2]
        # 
        """ tim kiem thanh cong """
        if O.coordinates[0] == End[0] and O.coordinates[1] == End[1]:
            print('tim kiem thanh cong')
            handle.main_route(O, route)
            return O
        
        """ Tim vitri O trong matrix """
        index = 0
        for i in matrix:
            if i[0] == O.coordinates:
                index = matrix.index(i)

        for i in matrix[index]:
            # distance = math.sqrt((i[0] - End[0]) ** 2 + (i[1] - End[1]) ** 2) + O.cost + 1
            distance = math.sqrt(abs(i[0] - End[0]) + abs(i[1] - End[1])) + O.cost + 1
            tmp = handle.Node(i, None, O.cost + 1, distance)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                open.append(tmp)
                route_astar.append(tmp.coordinates)
                visited[i[0]][i[1]] = True