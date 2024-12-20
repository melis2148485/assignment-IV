'''In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u has, or equivalently, 
the number of edges incident upon it.
Given: A simple graph with n≤103 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the degree of vertex i.'''
#degree of a vertex is the number of edges connected to it(edges are connections between nodes)
def calculate_degrees(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        n,m=map(int, first_line.split())# each line is a string that we divide into 2 integers
        D=[0]*(n+1)# initialize array of degrees
        for line in file:
            u,v=map(int, line.strip().split())
            D[u]+=1
            D[v]+=1 #edge count increases by 1 each time vertex u or v is connected to a new edge
        return D[1:]#exclude the zero index
filename="deg.txt"
degrees=calculate_degrees(filename)
print(' '.join(map(str, degrees)))