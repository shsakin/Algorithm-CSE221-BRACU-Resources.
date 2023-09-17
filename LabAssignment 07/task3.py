def find_parent(parents,node):
    if parents[node]==node: return node
    else: return find_parent(parents,parents[node])

def make_friends(friends,parents,a,b):
    par_a=find_parent(parents,a)
    par_b=find_parent(parents,b)
    if par_a!=par_b:
        parents[par_b]=par_a
        friends[par_a]+=friends[par_b]
    return friends[par_a]


inp=open('input3.txt','r')
out=open('output3.txt','w')
n, m = map(int, inp.readline().split())
parents=[i for i in range(n+1)]
friends=[1]*(n+1)
for i in range(m):
    if i==m-1:
        newline=''
    else: newline='\n'
    a,b=map(int, inp.readline().split())
    result=make_friends(friends,parents,a,b)
    out.write(f'{result}{newline}')

inp.close()
out.close()

# made a parent array initializing every node to be its own parent, and friends array to count friends, when 2 nodes made friendship we made one's parent as other node
# and increament the parent's node's friend count+ child's node's friend, every time return thre parent node friend count from the friends array.  