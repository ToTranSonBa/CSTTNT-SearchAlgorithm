import handle

def dfs(matrix, bonus_points, Start, End, visited, route, route_dfs):
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
        O = open.pop(-1)
        route_dfs.append(O.coordinates)
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
            tmp = handle.Node(i)
            tmp.par = O
            if visited[i[0]][i[1]] == False:
                open.append(tmp)
                visited[i[0]][i[1]] = True
