def preRequisite_DFS(G,course,colour,order):
    colour[course]=1
    for v in G[course]:
        if colour[v]==0:
            preRequisite_DFS(G,v,colour,order)
    order.append(course)

def preRequisite_order(G,colour,order):
    for course in range(1,len(G)):
        if not Check_inDegree(G,course):
            if colour[course]==0:
                preRequisite_DFS(G,course,colour,order)
    return order[::-1]


def Check_inDegree(G,value):
    return True if any(value in nested for nested in G) else False

inp=open('input1a.txt','r')
out=open('output1a.txt','w')
n,m=inp.readline().split()
adj_list=[[]for _ in range(int(n)+1)]
for _ in range(int(m)):
    u,v=inp.readline().split()
    adj_list[int(u)].append(int(v))

colour=[0]*(int(n)+1)
order=[]
Final_order=preRequisite_order(adj_list,colour,order)
if len(Final_order)==int(n):
    for course in Final_order:
        out.write(f'{course} ')
else: out.write('IMPOSSIBLE')

# for finding the pre requisites started traversing the graph only with the nodes that has zero in degrees, that means they are the prerequisites. 
# and traversed the node to its depth with DFS algorithm.