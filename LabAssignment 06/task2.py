import heapq
def Dijkstra(G,W,S):
    distance=[float('inf')]*len(G)
    distance[S]=0
    pq=[]
    heapq.heappush(pq,S)
    while pq:
        cur_node=heapq.heappop(pq)
        for u in G[cur_node]:
            if distance[cur_node]+W[cur_node][u][0]<distance[u]:
                distance[u]=distance[cur_node]+W[cur_node][u][0]
                heapq.heappush(pq,u)
    return distance

inp=open('input2.txt','r')
out=open('output2.txt','w')
n,m=inp.readline().split()
adj_list=[[] for _ in range(int(n)+1)]
adj_weight=[[[]for _ in range(int(n)+1)] for _ in range(int(n)+1)]
for i in range(int(m)):
    u,v,w=inp.readline().split()
    adj_list[int(u)].append(int(v))
    adj_weight[int(u)][int(v)].append(int(w))

S,T=inp.readline().split()
Alice_path=Dijkstra(adj_list,adj_weight,int(S))
Bob_path=Dijkstra(adj_list,adj_weight,int(T))
minimum_time=float('inf')
meeting_node=0
for node in range(1,int(n)+1):
    if Alice_path[node]!=float('inf') and Bob_path[node]!=float('inf'):
        time=max(Alice_path[node],Bob_path[node])
        if time<minimum_time:
            minimum_time=time
            meeting_node=node

if meeting_node==0:
    out.write('Impossible')
else: out.write(f'TIme: {minimum_time}\nNode: {meeting_node}')

inp.close()
out.close()

# implemented the dijkstra algorithm from alice's source and from bob's source, and took the common and fastest cost node from each path. 
