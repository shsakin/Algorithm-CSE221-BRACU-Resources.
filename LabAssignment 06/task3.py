import heapq
def Prim(G,W,S):
    distance=[float('inf')]*len(G)
    colour=[0]*len(G)
    distance[S]=0
    pq=[]
    heapq.heappush(pq,S)
    while pq:
        cur_node=heapq.heappop(pq)
        for u in G[cur_node]:
            if colour[u]==0:
                if W[cur_node][u][0]<distance[u]:
                    distance[u]=W[cur_node][u][0]
                    heapq.heappush(pq,u)
    return distance

inp=open('input3.txt','r')
out=open('output3.txt','w')
n,m=inp.readline().split()
adj_list=[[] for _ in range(int(n)+1)]
adj_weight=[[[]for _ in range(int(n)+1)] for _ in range(int(n)+1)]
for i in range(int(m)):
    u,v,w=inp.readline().split()
    adj_list[int(u)].append(int(v))
    adj_weight[int(u)][int(v)].append(int(w))

distance=Prim(adj_list,adj_weight,1)
if distance[int(n)]==float('inf'):
    minimum_difficulty='Impossible'
else:
    minimum_difficulty=str(max(distance[1:]))

out.write(minimum_difficulty)

inp.close()
out.close()

# implemented the prim's algorithm, this algorithm find the minimum cost in every possible path from source but only update the minimum cost in the distance array, 
# as prim gives the minimum cost of every node so the maximum of the minimum cost is the safest path, and if the node remains infinity then the node is unreachable.
