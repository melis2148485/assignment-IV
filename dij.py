'''Given: A simple directed graph with positive edge weights from 1 to 103 and n≤103 vertices in the edge 
list format.
Return: An array D[1..n]where D[i]is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). 
If i is not reachable from 1 set D[i]to −1'''
import networkx as nx
def read_input(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        while not first_line:
            first_line = file.readline().strip()
        n,m=map(int, first_line.split())#extract only nodes, ignoring edges, here not needed
        edges=[]
        for line in file:
            line = line.strip()
            if not line:  # if empty line loop continues to the next
                continue
            u,v,w=map(int, line.strip().split())#u=starting vertex of edge, v=ending vertex of edge, w=weight of edge between u and w vertices 
            edges.append((u,v,w))
    return n, edges
def  dijkstra_shortest_path(filename):
    n, edges=read_input(filename)
    graph=nx.DiGraph()#directed graph
    graph.add_weighted_edges_from(edges)
    if 1 in graph.nodes:#compute shortest paths staring from node 1
        shortest_paths=nx.single_source_dijkstra_path_length(graph, source=1)
    else:
        shortest_paths={}
    D=[-1]*(n+1)#initialize all distancs as -1 
    for node in range(1, n+1):
        if node ==1:
            D[node]=0#if the current vertex is the source vertex, its distance to itslef is equal zero
        elif node in shortest_paths:
            D[node]=shortest_paths[node]#the vertex is reachable from vertex 1 because is found in shortest_paths so we set distance 
            #from this vertex to the value found in shortest_paths
    return D[1:]
def main():
    filename="dij.txt"
    result=dijkstra_shortest_path(filename)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
