# Finding Minimum Spanning Tree with Prim's Algorithms
# initialize infinity value
infinity = 99999999
# initialize total number of nodes
nbr_of_nodes = 7
# adjacency matrix
graph = [[0, 28, 0, 0, 0, 10, 0],
         [28, 0, 16, 0, 0, 0, 14],
         [0, 16, 0, 12, 0, 0, 0],
         [0, 0, 12, 0, 22, 0, 18],
         [0, 0, 0, 22, 0, 25, 24],
         [10, 0, 0, 0, 25, 0, 0],
         [0, 14, 0, 18, 24, 0, 0]]
# list value is changed to true when node is selected
min_spanning_tree = [0, 0, 0, 0, 0, 0, 0]

# Counter for number of edges
nbr_of_edges = 0

# change the first value of the list
min_spanning_tree[0] = True

# Loop through while edges are less than total vertices - 1
while nbr_of_edges < nbr_of_nodes - 1:
    # initialize minimum to infinity for each edges
    minimum = infinity
    # set two variables to zero to print answer
    x = 0
    y = 0
    for i in range(nbr_of_nodes):
        if min_spanning_tree[i]:
            for j in range(nbr_of_nodes):
                if (not min_spanning_tree[j]) and graph[i][j]:
                    # if node is not in MST list and we take note of an edge
                    if minimum > graph[i][j]:
                        minimum = graph[i][j]
                        x = i
                        y = j
    print("Nodes: " + str(x) + "-" + str(y) + " with the weight " + str(graph[x][y]))
    min_spanning_tree[y] = True
    # increment the number of edges through each loop through
    nbr_of_edges += 1
    # print to check everytime a node is found
    print(min_spanning_tree)
