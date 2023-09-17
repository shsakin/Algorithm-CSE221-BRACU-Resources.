import heapq
def preRequisite_BFS(G):
    colour=[0]*len(G)
    priority_q=[]
    path=[]
    for i in range(1,len(G)):
        if G[i]:
            if not Check_inDegree(G,i):
                heapq.heappush(priority_q,i)
    while priority_q:
        u=heapq.heappop(priority_q)
        path.append(u)
        i=0
        for v in G[u]:
            if colour[v]==0: 
                if Check_inDegree((G[:u]+G[u+1:]),v):
                    G[u]=G[u][:i]+G[u][i+1:]
                else:    
                    colour[v]=1
                    heapq.heappush(priority_q,v)
                    i+=1
    return path

def Check_inDegree(G,value):
    return True if any(value in nested for nested in G) else False

inp=open('input2.txt','r')
out=open('output2.txt','w')
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

# used the same strategy as BFS (task1b) but as the goal is to find the lexicographically small path so used a priority queue instead of a regular queue
# priority queue always dequeues the smallest value so thats how we get the lexicographically small path.