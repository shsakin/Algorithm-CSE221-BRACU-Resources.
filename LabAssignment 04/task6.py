def diamond_heist(G,row,column):
    global diamond_count
    if row>=r or column>=h or row<0 or column<0:
        return 
    if G[row][column]=='#':
        return
    if G[row][column]=='D':
        diamond_count+=1
    visited[row][column]=1

    if visited[row+1][column]==0:
        diamond_heist(G,row+1,column)
    if visited[row][column+1]==0:
        diamond_heist(G,row,column+1)
    if visited[row-1][column]==0:
        diamond_heist(G,row-1,column)
    if visited[row][column-1]==0:
        diamond_heist(G,row,column-1)
        

inp=open('input6.txt','r')
out=open('output6.txt','w')
global r,h,visited
r,h=[int(i) for i in inp.readline().split()]
adj_matrix=[]
for i in range(r):
    temp=inp.readline()
    adj_matrix.append(temp)

visited=[[0]*(h+1) for _ in range(r+1)]
max_diamond=0
for i in range(r):
    for j in range(h):
        diamond_count=0
        diamond_heist(adj_matrix,i,j)
        if diamond_count>max_diamond:
            max_diamond=diamond_count

out.write(str(max_diamond))

inp.close()
out.close()


# for this task we create a multi-dimensional list exactly of the size
# of the input to keep track of the visited cell, we start from a cell
# and unless we find obstacle or row or column of the input exceeds,
# we keep travering increasing and decreasing the row and column numbers
# and this happens recursively, and we start the traversing from every
# staring position possible (every node) for finding the maximum amounts
# of diamonds.
