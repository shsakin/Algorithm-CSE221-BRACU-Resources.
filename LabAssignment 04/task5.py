from queue import Queue
def BFS(G,S):
    parents=[None]*len(G)
    time=['inf']*(len(G))
    q=Queue()
    time[S]=0
    q.put(S)
    while q.qsize()!=0:
        u=q.get()
        for v in G[u]:
            if time[v]=='inf':
                time[v]=time[u]+1
                parents[v]=u
                q.put(v)
    return parents,time

def shortest_time_tracker(G,start,destination):
    parents,time=BFS(G,start)
    path=[]
    path.append(destination)
    current=destination
    while parents[current]!=None:
        path.append(parents[current])
        current=parents[current]
    return list(reversed(path)),time[destination]

inp=open('input5.txt','r')
out=open('output5.txt','w')
n,m,d=[int(i) for i in inp.readline().split()]
adj_list=[[]for _ in range(n+1)]
for i in range(m):
    u,v=[int(i) for i in inp.readline().split()]
    adj_list[u].append(v)
    adj_list[v].append(u)

shortest_path,time=shortest_time_tracker(adj_list,1,d)
out.write(f'Time: {time}\n')
out.write('Shortest Path: ')
for nodes in shortest_path:
    out.write(f'{nodes} ')


inp.close()
out.close()
    
# for finding the shortest path and the time to get there, we first
# traverse the graph using BFS, and we keep track the distance to each
# node from the start position and also keep track each parents node
# using the distance and parents array, then after running the bfs
# we use the parents array and start traversing in the destination's
# parents all the way to the start position, thats how we get the
# reverse list of the shortest path so we return it after reversing
# it and also return the time of the destination from the distance array.

