'''Given: A positive integer n(n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.
Return: The minimum number of edges that can be added to the graph to produce a tree.'''
import networkx as nx
def read_input(filename):
    with open(filename,"r") as file:
        lines=file.readlines()
    n=int(lines[0].strip())#n of nodes
    edges=[]
    for line in lines[1:]:
        u,v=map(int, line.strip().split())
        edges.append((u,v))#add edges as tuples
    return n, edges
def min_edges(n, edges):
    G=nx.Graph()
    G.add_nodes_from(range(1,n+1))#add nodes 1 trough n
    G.add_edges_from(edges)#add edges from list
    n_components=nx.number_connected_components(G)#find number of connected components
    return n_components-1#minimum number of edges to connect graph from a tree
def main():
    filename="tree.txt"
    n, edges=read_input(filename)
    final_edges=min_edges(n, edges)
    print(final_edges)

if __name__ == '__main__':
    main()