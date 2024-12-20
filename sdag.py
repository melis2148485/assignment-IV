'''Given: A weighted DAG with integer edge weights from −103 to 103 and n≤105 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i
is not reachable from 1 set D[i] to x.'''
#There are two subclasses of graphs that automatically exclude the possibility of negative cycles: graphs without negative edges, 
#and graphs without cycles. We will now see how the single-source shortest-path problem can be solved in just linear time on 
#directed acyclic graphs.
#Perform a sequence of updates (recall Bellman-Ford algorithm) that includes every shortest path as a subsequence. The key source 
# of efficiency is that  the vertices appear in increasing linearized order.
#we linearize  the DAG by depth-first search, and then visit the vertices in sorted order, updating the edges out of each. 
import networkx as nx
def read_input(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        n,m=map(int, first_line.split())
        edges=[]
        for _ in range(m):
            edge_line=file.readline().strip()
            while not edge_line:
                edge_line=file.readline().strip()
            u,v,w=map(int, edge_line.split())
            edges.append((u,v,w))
    return n, edges

def  shortest_paths(n, edges):
    graph=nx.DiGraph()#directed graph
    graph.add_weighted_edges_from(edges)
    topological_order=list(nx.topological_sort(graph))#list stores vertices in their topological order, so when u->v, u comes before v
    
    D={1:0}#initialize distances indicating they are compared to the source

    for u in topological_order:
        if u in D:
            for v, attr in graph[u].items():
                weight=attr['weight']
                if v not in D or D[u]+weight<D[v]:
                    D[v]=D[u]+weight
    result=[D[i] if i in D else 'x' for i in range(1,n+1)]
    return result
    
def main():
    filename="sdag.txt"
    n, edges=read_input(filename)
    result=shortest_paths(n, edges)
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
