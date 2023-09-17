import numpy as np
inp=open('input1a.txt','r')
out=open('output1a.txt','w')
n,m=[int(i) for i in inp.readline().split()]
adj_matrix=np.zeros((n+1,n+1),dtype=int)
for i in range(m):
    u,v,w=[int(i) for i in inp.readline().split()]
    adj_matrix[u][v]=w

for i in range(n+1):
    newline='' if i==n else '\n'
    for j in range(n+1):
        out.write(f'{adj_matrix[i][j]} ')
    out.write(newline)
        
inp.close()
out.close()



# for this task we simply created an array of zeroes using numpy of
# (n+1*n+1) dimention, and simply put the value of the nodes accordingly 
# into the matrix.  