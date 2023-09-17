from queue import Queue
def detect_cycle(G,S):
    colour=[0]*len(G)
    q=Queue()
    colour[S]=1
    q.put(S)
    while q.qsize()!=0:
        u=q.get()
        for v in G[u]:
            if v==S:
                return True
            elif colour[v]==0:
                colour[v]=1
                q.put(v)
                
    return False

inp=open('input4.txt','r')
out=open('output4.txt','w')
n,m=[int(i) for i in inp.readline().split()]
adj_list=[[]for _ in range(n+1)]
for i in range(m):
    u,v=[int(i) for i in inp.readline().split()]
    adj_list[u].append(v)
for i in range(1,n+1):
    val=detect_cycle(adj_list,i)
    if val:
        break
if val:
    out.write('YES')
else:
    out.write('NO')

inp.close()
out.close()

# for detecing cycle in a graph if we find a node twice than its a cycle
# so we start traversing the graph using BFS with all of the nodes
# (every starting position possible) that way if the traversal find the
# starting node twice it will return True, otherwise False.