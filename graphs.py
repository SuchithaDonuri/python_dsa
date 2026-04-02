def has_cycle(graph):

    visited = set()   # mark the visiting node

    def dfs(node, parent):  # it passes current node and parent(where it came from)
        visited.add(node)   # add the node to visited set

        for neighbour in graph[node]: # loops through neigbour nodes in the graph nodes 0,1,2,3, graph[0] = [1, 2]

            if neighbour not in visited:    # graph[0] = [1, 2] , 1 not in {0}
                if dfs(neighbour, node):   # dfs(1,0) we go to one neighbor and then check that neighbors neighbors (go deep)
                    return True

            elif neighbour != parent:     
                return True

        return False   

    
    for node in graph:   # Loop through all nodes 0,1,2,3
        if node not in visited:     #initally visited is empty first 0,1,2,3
            if dfs(node, -1):
                return True

    return False


# Test
# graph = {
#     0: [1, 2],
#     1: [0, 3],
#     2: [0, 3],
#     3: [1, 2]
# }
graph = {
0: [1],
1: [0, 2],
2: [1]
}

print(has_cycle(graph))