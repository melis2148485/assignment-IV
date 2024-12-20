'''The task is to use Bellman-Ford algorithm to check whether a given graph contains a cycle of negative weight.
Given: A positive integer k≤20 and k simple directed graphs with integer edge weights from −103 to 103 and n≤103 vertices 
in the edge list format.
Return: For each graph, output "1" if it contains a negative weight cycle and "-1" otherwise.'''
import networkx as nx
def read_input(filename):

    with open(filename,'r') as file:
        first_line=file.readline().strip()
        while not first_line:
            first_line = file.readline().strip()
        k=int(first_line)# number of graphs

        graphs=[]
        for _ in range(k):#loop trough graphs
            line = file.readline().strip()
            while not line:  
                line = file.readline().strip()
            n,m=map(int, line.split())#number of vertices and edges out of each graph 

            edges=[]
            for _ in range(m):#loop through edges
                edge_line = file.readline().strip()
                while not edge_line:  
                    edge_line=file.readline().strip()
                u, v, w=map(int, edge_line.split())
                edges.append((u,v,w))
            graphs.append(edges)
    return graphs

def check_negative_weigth_cycle(graphs):#if a negative cycle in the graph exists, function returns 1, otherwise -1
    results=[]
    for edges in graphs:
        graph=nx.DiGraph()
        graph.add_weighted_edges_from(edges)

        if nx.negative_edge_cycle(graph, weight="weight") : #check if there's a negative cycle
            results.append(1)
        else:#when no path exists
            results.append(-1)
    return results
def main():
    filename="nwc.txt"
    graphs=read_input(filename)
    results=check_negative_weigth_cycle(graphs)
    print(' '.join(map(str, results)))
    
if __name__=="__main__":
    main()


