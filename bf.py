'''Given: A simple directed graph with integer edge weights from −103 to 103 and n≤103 vertices in 
the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i
(D[1]=0). If i is not reachable from 1 set D[i]to x.'''
#we compute the shortest path from vertex 1 to all the other vertices and build an array with the shortest sequences
import networkx as nx

def read_input(filename):
    with open(filename,'r') as file:
        first_line = file.readline().strip()
        n, m=map(int, first_line.split())# extract n, so vertices and m, so edges
        edges=[]
        for line in file:
            line=line.strip()
            if not line:#skipping empty lines
                continue
            u,v,w=map(int, line.split())
            edges.append((u,v,w))
    return n, edges

def bf_shortest_path(filename):
    n, edges=read_input(filename)
    graph=nx.DiGraph()
    graph.add_weighted_edges_from(edges)
    if 1 in graph.nodes:#compute shortest paths staring from node 1
        shortest_paths=nx.single_source_bellman_ford_path_length(graph, source=1)
    else:
        shortest_paths={}
    D=['x']*(n+1)#initialize distance array with special value x, indicating the unreachable vertices
    for node in range(1, n+1):
        if node ==1:
            D[node]=0
        elif node in shortest_paths:
            D[node]=shortest_paths[node]
    return D[1:]
def main():
    filename="bf.txt"
    result=bf_shortest_path(filename)
    print(' '.join(map(str, result)))
if __name__=="__main__":
    main()
