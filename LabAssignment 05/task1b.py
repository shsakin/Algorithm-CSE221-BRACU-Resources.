from queue import Queue
def preRequisite_BFS(G):
    colour=[0]*len(G)
    q=Queue()
    path=[]
    for i in range(1,len(G)):
        if G[i]:
            if not Check_inDegree(G,i):
                q.put(i)
    while q.qsize()!=0:
        u=q.get()
        path.append(u)
        i=0
        for v in G[u]:
            if colour[v]==0: 
                if Check_inDegree((G[:u]+G[u+1:]),v):
                    G[u]=G[u][:i]+G[u][i+1:]
                else:    
                    colour[v]=1
                    q.put(v)
                    i+=1
    return path

def Check_inDegree(G,value):
    return True if any(value in nested for nested in G) else False

inp=open('input1b.txt','r')
out=open('output1b.txt','w')
n,m=inp.readline().split()
adj_list=[[]for _ in range(int(n)+1)]
for _ in range(int(m)):
    u,v=inp.readline().split()
    adj_list[int(u)].append(int(v))

order=preRequisite_BFS(adj_list)

if len(order)==int(n):
    for courses in order:
        out.write(f'{courses} ')
else:
    out.write('IMPOSSIBLE')

# for finding the pre requisite with BFS, first we only put the nodes into the queue that has zero indegree, then like BFS we traverse the dequeued nodes, if the node has an indegree
# we remove the node from there (used slicing for removing as .remove() or .pop() hampers the loop.), removed it beacause the next time we check the indegree of the node it returns False.
# and then gradually put the remaining nodes into the queue and traverse it.

