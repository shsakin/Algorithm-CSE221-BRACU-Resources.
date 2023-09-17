inp=open('input1b.txt','r')
out=open('output1b.txt','w')
n,m=[int(i) for i in inp.readline().split()]
adj_list=[[]for _ in range(n+1)]
for i in range(m):
    u,v,w=[int(i) for i in inp.readline().split()]
    adj_list[u].append((v,w))


for i in range(len(adj_list)):
        newline='' if i==n else '\n'
        if adj_list[i]==[]:
            out.write(f'{i}: ')
            out.write(f'{newline}')
            
        else:
            out.write(f'{i}: ')
            for j in adj_list[i]:
                out.write(f'{j} ')
            out.write(f'{newline}')
            
inp.close()
out.close()   

# for creating a adjacency list we used list comprehension for creating
# an empty multidimensional list and put the value of v and w into the
# array's u index, and showing the each nodes's value as a tuple.
            