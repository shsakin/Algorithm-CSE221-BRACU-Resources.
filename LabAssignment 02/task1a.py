inp=open('input1a.txt','r')
len_int=[int(i) for i in inp.readline().split()]
val=len_int[1]
array=[int(i) for i in inp.readline().split()]
out=open('output1a.txt','w')
flag=True
for i in range(len_int[0]):
    for j in range(i+1,len_int[0]):
        if array[i]+array[j]==val:
            flag=False
            out.write(f'{i+1} {j+1}')
            break
    if not flag:
        break
if flag:
    out.write('IMPOSSIBLE')

inp.close()
out.close()


