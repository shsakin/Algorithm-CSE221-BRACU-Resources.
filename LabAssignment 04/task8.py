from queue import Queue
def modified_BFS(G,S):
    global colour
    vampires=[]
    lykans=[]
    q=Queue()
    if S not in colour:
        colour.append(S)
        vampires.append(S)
        q.put(S)
    while q.qsize()!=0:
        u=q.get()
        for v in G[u]:
            if v not in colour:
                colour.append(v)
                q.put(v)
                if u in vampires:
                    lykans.append(v)
                else:
                    vampires.append(v)
            
    return vampires,lykans

#took input no. 1 from the debug section in LightOJ
inp=open('input8.txt','r')
out=open('output8.txt','w')
test_case=int(inp.readline())
for tests in range(test_case):
    newline='' if tests==test_case-1 else '\n' 
    n=int(inp.readline()) 
    graph={}
    for _ in range(n):
        u,v=[int(i) for i in inp.readline().split()]
        if u not in graph:
            graph[u]=[v]
        else:
            graph[u].append(v)
        if v not in graph:
            graph[v]=[u]
        else:
            graph[v].append(u)

    max_number=0
    colour=[]
    for starts in graph.keys():
        vampires,lykans=modified_BFS(graph,starts)
        max_number+=max(len(vampires),len(lykans))

    out.write(f'Case {tests+1}: {max_number}{newline}')
        

inp.close()
out.close()
    

# for this we used dictinary to represent the graph as the nodes can be
# too large as a number, so we traverse the graph from each of the nodes
# and mark them as either lykan or vampire as in the a node is lykan
# its parent or children would be vampire, we used a global colour array
# to keep track the visited nodes we dont want any nodes to be visited twice
# we took the maximum number from the vampire and lykans and keep adding
# into the max_number thats how we get the highest number of lykans or vampires. 
