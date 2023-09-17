def TopSorting_DFS(G,source,colour,stack):
    colour[source]=1
    for u in G[source]:
        if colour[u]==0:
            TopSorting_DFS(G,u,colour,stack)
    stack.append(source)

def DFS_traverse(G,source,colour,components):
    colour[source]=1
    components.append(source)
    for u in G[source]:
        if colour[u]==0:
            DFS_traverse(G,u,colour,components)

def transpose_graph(G):
    transpose_graph=[[]for _ in range(len(G))]
    for u in range(1,len(G)):
        for v in G[u]:
            transpose_graph[v].append(u)
    return transpose_graph

def SCC(G,Top_sorted):
    colour=[0]*len(G)
    transposeGraph=transpose_graph(G)
    connceted_components=[]
    while Top_sorted:
        components=[]
        curr_node=Top_sorted.pop()
        if colour[curr_node]==0:
            DFS_traverse(transposeGraph,curr_node,colour,components)
            connceted_components.append(sorted(components))
    return connceted_components

inp=open('input3.txt','r')
out=open('output3.txt','w')
n,m=inp.readline().split()
adj_list=[[]for _ in range(int(n)+1)]
for _ in range(int(m)):
    u,v=inp.readline().split()
    adj_list[int(u)].append(int(v))
colour=[0]*(int(n)+1)
stack=[]
for source in range(1,int(n)+1):
    if colour[source]==0:
        TopSorting_DFS(adj_list,source,colour,stack)
strongly_connected_components=sorted(SCC(adj_list,stack))
newline_count=0
for components in strongly_connected_components:
    newline_count+=1
    if newline_count==len(strongly_connected_components):
        newline=' '
    else:
        newline='\n'
    out.write(' '.join(str(vertex) for vertex in components))
    out.write(newline)

# we tracked the topological order of the graph then tranposed the graph and traverse according the topological order, then looked for the cycle nodes and tracked the nodes
# so the cycled nodes are strongly connected nodes and the remainings the single SCC nodes.