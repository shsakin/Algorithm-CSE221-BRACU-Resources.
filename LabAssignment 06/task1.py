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

inp=open('input1.txt','r')
out=open('output1.txt','w')
n,m=inp.readline().split()
adj_list=[[] for _ in range(int(n)+1)]
adj_weight=[[[]for _ in range(int(n)+1)] for _ in range(int(n)+1)]                              #made the weighted adj list with 3d array.
for i in range(int(m)):
    u,v,w=inp.readline().split()
    adj_list[int(u)].append(int(v))
    adj_weight[int(u)][int(v)].append(int(w))
    

source= inp.readline()
distance=Dijkstra(adj_list,adj_weight,int(source))

for i in range(1,len(distance)):
    if distance[i]==float('inf'):
        distance[i]=-1
    out.write(f'{distance[i]} ')

inp.close()
out.close()

# implemented the dijkstra algorithm, dijkstra algorithm find the shortest path from the source node, here if the distance remains infinity that means the node is unreachable from the source so made it -1.
