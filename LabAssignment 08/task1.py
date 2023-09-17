def Kruskal(adj_list,parents):
    cost=0
    adj_list.sort(key=lambda x: x[2])
    for u,v,w in adj_list:
        parent_u = find_parent(parents,u)
        parent_v = find_parent(parents,v)
        if parent_u!=parent_v:
            parents[parent_u] = parent_v
            cost+=w
    return cost

def find_parent(parents,u):
    if parents[u]==u:
        return u
    return find_parent(parents,parents[u])

inp=open('input1.txt','r')
out=open('output1.txt','w')
m,n=map(int,inp.readline().split())
adj_list=[]
for i in range(n):
    u,v,w=map(int,inp.readline().split())
    adj_list.append((u,v,w))

parents=[i for i in range(m+1)]
result=Kruskal(adj_list,parents)

out.write(f'{result}')

inp.close()
out.close()

# kruskal algorithm, sorted the adj_list ascending to the weight, by default every node is its own parent, so when two node's parents dont match we set the u node's parent to v,
# add cost every time each other's parent dont match (that means they are not connected), other wise do not add cost.