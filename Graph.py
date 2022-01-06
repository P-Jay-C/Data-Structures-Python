def add_node(V):

    global node_count
    
    if V in nodes:
        print(v, " is already present in the graph")
    else:
        node_count = node_count + 1
        nodes.append(V)

        for n in graph:
             n.append(0)


        temp = []
        for i in range(node_count):
            temp.append(0)

        graph.append(temp)

def add_edge(V1,V2):
    if V1 not in nodes:
        print(V1, " is not present in the graph")
    elif V2 not in nodes:
        print(V2, " is not present in the graph")
    else:
        index1 = nodes.index(V1)
        index2 = nodes.index(V2)

        graph[index1][index2]=1
        graph[index2][index1] = 1

def DFS(node,visited,graph):

    if node not in graph:
        print("Node is not present in the graph")
        return

    
    if node not in visited:
        print (node)

        visited.add(node)

        for i in graph[node]:
            DFS(i, visited, graph)  

    
def print_graph():

    print()
    
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j],"<3"),end = " ")
        print()

nodes = []
graph = []

node_count = 0
visited  = set()

print("Before adding nodes")
print(nodes, end = " ")
 

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A","B")
add_edge("A","C")
add_edge("A","D")
add_edge("C","D")
add_edge("B","D")
add_edge("B","E")
add_edge("D","E")


print("After adding nodes")

DFS("A", visited, graph)
