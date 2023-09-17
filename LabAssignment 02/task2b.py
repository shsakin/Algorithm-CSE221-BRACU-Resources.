def merge(a1,a2):
    sorted_arr=[0]*(len(a1)+len(a2))
    i,j,k=0,0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            sorted_arr[k]=a1[i]
            i+=1
        else:
            sorted_arr[k]=a2[j]
            j+=1
        k+=1
    while i<len(a1):
        sorted_arr[k]=a1[i]
        i+=1
        k+=1
    while j<len(a2):
        sorted_arr[k]=a2[j]
        j+=1
        k+=1
    
    return sorted_arr


inp=open('input2b.txt','r')
out=open('output2b.txt','w')
length1=int(inp.readline())
array1=[int(i) for i in inp.readline().split()]
length2=int(inp.readline())
array2=[int(i) for i in inp.readline().split()]
sortedarr=merge(array1,array2)
for i in sortedarr:
    out.write(f'{i} ')
inp.close()
out.close()

