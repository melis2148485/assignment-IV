'''Given: A positive integer k≤20 and k simple directed graphs with positive integer edge weights and at most 103 vertices 
in the edge list format.
Return: For each graph, output the length of a shortest cycle going through the first specified edge if there is a cycle 
and "-1" otherwise.'''
import networkx as nx
def read_input(filename):

    with open(filename,'r') as file:
        first_line=file.readline().strip()
        while not first_line:
            first_line = file.readline().strip()
        k=int(first_line)#extract number of graphs

        graphs=[]
        for _ in range(k):
            line = file.readline().strip()
            while not line:  # Skip empty lines
                line = file.readline().strip()
            n,m=map(int, line.split())#extract vertices and edges out of each graph 

            edges=[]
            for _ in range(m):
                edge_line = file.readline().strip()
                while not edge_line:  # Skip empty lines
                    edge_line=file.readline().strip()
                u, v, w=map(int, edge_line.split())
                edges.append((u,v,w))
            graphs.append(edges)
    return graphs

def shortest_cycle(graphs):
    results=[]
    for edges in graphs:
        u,v,w=edges[0]

        graph=nx.DiGraph()
        graph.add_weighted_edges_from(edges)

        graph.remove_edge(u,v)#the first edge is removed temporarily, since we are finding the shortest cycle, so the for loop goes 
        #into a closed path that starts from the first node, travels through the  other nodes and comes back to the first
        #find shortest paths from v
        shortest_paths=nx.single_source_dijkstra_path_length(graph, source=v, weight='weight')#parameters:graph where you calculate 
        #the shortest path length, source is the starting node from where you count, weigth value referring to edge's value
        if u in shortest_paths: #check if there's a path from v back to u
            cycle_length=shortest_paths[u]+w#if there's a path from v bacj to u, calculate its length
            results.append(cycle_length)
        else:#when no path exists
            results.append(-1)
        graph.add_edge(u,v,weight=w)
    return results

def main():
    filename="cte.txt"
    graphs=read_input(filename)
    results=shortest_cycle(graphs) 
    print(' '.join(map(str, results))) 
if __name__=="__main__":
    main()

