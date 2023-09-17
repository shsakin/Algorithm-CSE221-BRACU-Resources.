from queue import Queue
def longest_path(G,S):
    distance=['inf']*(len(G))
    q=Queue()
    distance[S]=0
    q.put(S)
    while q.qsize()!=0:
        u=q.get()
        for v in G[u]:
            if distance[v]=='inf':
                distance[v]=distance[u]+1
                q.put(v)
    distance.remove('inf')
    return distance.index(max(distance))+1,max(distance)

inp=open('input7.txt','r')
out=open('output7.txt','w')
cities=int(inp.readline())
adj_list=[[]for _ in range(cities+1)]
for i in range(cities-1):
    u,v=[int(i) for i in inp.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)

max_distance=0
starting_city=0
ending_city=0
for i in range(1,cities):
    ending,distance=longest_path(adj_list,i)
    if distance>max_distance:
        max_distance=distance
        starting_city=i
        ending_city=ending

out.write(f'{starting_city} {ending_city}')

inp.close()
out.close()



# in this task its basically finding the longest path without any repeated
# paths, as we can track the distance of the nodes using bfs so return
# the index of the max distance as it will be ending city, and as we
# start travering from every possible starting position, so which of the
# start gives the max distance will be the starting city. 
