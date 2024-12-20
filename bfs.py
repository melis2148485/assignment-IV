'''Given: A simple directed graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i]is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0).
If i is not reachable from 1set D[i] to −1.'''
import networkx as nx
def find_shortest_path(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        n,_=map(int, first_line.split())
        edges=[]
        for line in file:
            u,v=map(int, line.strip().split()) 
            edges.append((u,v))
    graph=nx.DiGraph()#directed graph
    graph.add_edges_from(edges)
    if 1 in graph.nodes:#compute shortest paths staring from node 1
        shortest_paths=nx.single_source_shortest_path_length(graph, source=1)
    else:
        shortest_paths={}
    distances=[-1]*n#initialize all distances as -1 
    for node, distance in shortest_paths.items():
        distances[node-1]=distance#update distance for reachable nodes, using nodes-1 because graph's nodes
        #are 1-indexed but we want them to be 0-indexed
    return distances
filename="bfs.txt"
result=find_shortest_path(filename)
print(' '.join(map(str, result)))
