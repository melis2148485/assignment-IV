'''Given: A simple graph with n≤103 vertices in the edge list format.
Return: An array D[1..n]where D[i]is the sum of the degrees of i's neighbors.'''
#we calculate first the degree(the number of edges)for each vertex, then calculate for each vertex the sum of degrees of its neighbors
def sum_degrees(filename):
    with open(filename,'r') as file:
        first_line=file.readline().strip()
        n,m=map(int, first_line.split())
        degree=[0]*(n+1)#to initialize array of degrees to keep track of each vertex
        neighbors_list=[[] for _ in range(n + 1)]#list to store neighbors for each vertex
        for line in file:
            u,v=map(int, line.strip().split())
            degree[u]+=1
            degree[v]+=1#as before, for each edge encountered we increment the number of degree for both vertices 
            neighbors_list[u].append(v)
            neighbors_list[v].append(u) #then add vertex v to the list of neighbors of u and viceversa
        D=[0]*(n+1)#result array
        for i in range(1,n+1):
            D[i]=sum(degree[neighbor]for neighbor in neighbors_list[i])#for each vertex i sum the degrees of its neighbors
        return D[1:]
filename="ddeg.txt"
final_result=sum_degrees(filename)
print(' '.join(map(str, final_result)))