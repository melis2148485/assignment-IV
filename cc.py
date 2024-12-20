'''Given: A simple graph with n≤103 vertices in the edge list format.
Return: The number of connected components in the graph.'''
#edge list format:The first line contains two numbers, the number of vertices n and the number of edges m, each of the following m
#lines contains an edge given by two vertices.
import networkx as nx
def counter_components(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        n,_=map(int, first_line.split()) #extract only vertices n, the number of edges m is not needed
        edges=[]#empty list to store edges
        for line in file:
            u,v=map(int, line.strip().split()) 
            edges.append((u,v))
    graph=nx.Graph()
    graph.add_edges_from(edges)#add edges stored in list to the graph
    graph.add_nodes_from(range(1,n+1))#adds allvertices included in the graph
    connected_components=nx.number_connected_components(graph)#function to count connected components
    return connected_components
filename="cc.txt"
tot_connected_components=counter_components(filename)
print(tot_connected_components)
  