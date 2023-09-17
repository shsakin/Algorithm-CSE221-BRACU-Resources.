from queue import Queue
def BFS(G,S,file):
    colour=[0]*len(G)
    q=Queue()
    colour[S]=1
    q.put(S)
    while q.qsize()!=0:
        u=q.get()
        file.write(f'{u} ')
        for v in G[u]:
            if colour[v]==0:
                colour[v]=1
                q.put(v)
        
    

inp=open('input2.txt','r')
out=open('output2.txt','w')
n,m=[int(i) for i in inp.readline().split()]
adj_list=[[]for _ in range(n+1)]
for i in range(m):
    u,v=[int(i) for i in inp.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)
    
BFS(adj_list,1,out)

inp.close()
out.close()

# for traversing the graph using BFS, we used adjacecty list and
# in the bfs function while dequeueing the value we printed the value
# to get the traversing order.






