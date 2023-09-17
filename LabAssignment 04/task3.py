def colourInitializing(G):
    global colour
    colour=[0]*len(G)

def DFS(G,u,file):
    colour[u] = 1
    file.write(f'{u} ')
    for i in G[u]:
        if colour[i]==0:
            DFS(G,i,file)

inp=open('input3.txt','r')
out=open('output3.txt','w')
n,m=[int(i) for i in inp.readline().split()]
adj_list=[[]for _ in range(n+1)]
for i in range(m):
    u,v=[int(i) for i in inp.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)

colourInitializing(adj_list)
DFS(adj_list,1,out)

inp.close()
out.close()

# for traversing the graph using DFS, we again used adjacency list
# used a different function outside dfs for the colour list to track the
# visited element, cannot do it inside the dfs function as it is a
# recursive function, and we print a the value at the start of the
# function to get the traversal order.