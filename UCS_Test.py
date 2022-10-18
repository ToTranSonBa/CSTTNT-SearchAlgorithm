import handle

def equal_coordinates(O, bonus_points):
    if O[0] == bonus_points[0] and O[1] == bonus_points[1]:
        return 1
    else: 
        return 0


def ucs(matrix, bonus_points, Start, End, visited, route, route_ucs):
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
        open.sort(key= lambda x: x.cost)
        O = open.pop(0)
        route_ucs.append(O.coordinates)

        # xu ly bonus
        for i in bonus_points:
            if equal_coordinates(O.coordinates, i) == 1:
                O.cost += i[2]
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
            tmp = handle.Node(i, None, O.cost + 1)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                open.append(tmp)
                visited[i[0]][i[1]] = True
