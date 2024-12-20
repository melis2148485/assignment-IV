'''Given: A positive integer k≤20and ksimple directed graphs in the edge list format with at most 103
vertices and 3⋅103edges each.
Return: For each graph, output "1" if the graph is acyclic and "-1" otherwise.'''

import networkx as nx
def read_input(filename):
    with open(filename,'r') as file:#file contains multiple graphs
        k=int(file.readline().strip())#n of graphs
        graphs=[]
        for _ in range(k):
            line = file.readline().strip()
            while not line:  # Skip empty lines
                line = file.readline().strip()
            n, m=map(int, line.split())#n of nodes and edges
            edges=[]
            for _ in range(m):
                u,v=map(int, file.readline().strip().split()) 
                edges.append((u,v))
            graphs.append(edges)
    return graphs

def check_ciclycity(graphs):
    results=[]
    for edges in graphs:
        graph=nx.DiGraph()
        graph.add_edges_from(edges)
        if nx.is_directed_acyclic_graph(graph):
            results.append(1)
        else:
            results.append(-1)
    return results

def main():
    filename="dag.txt"
    graphs=read_input(filename)
    results=check_ciclycity(graphs)
    print(' '.join(map(str, results)))

if __name__=="__main__":
    main()
