def merge(arr,a1,a2):
    i,j,k=0,0,0
    while i<len(a1) and j<len(a2):
        if a1[i]<=a2[j]:
            arr[k]=a1[i]
            i+=1
        else:
            arr[k]=a2[j]
            j+=1
        k+=1
    while i<len(a1):
        arr[k]=a1[i]
        i+=1
        k+=1
    while j<len(a2):
        arr[k]=a2[j]
        j+=1
        k+=1
    
    return arr

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        a1=mergeSort(arr[:mid])
        a2=mergeSort(arr[mid:])
        return merge(arr,a1,a2)

inp=open('input2a.txt','r')
out=open('output2a.txt','w')
length1=int((inp.readline()))
array1=[int(i) for i in inp.readline().split()]
length2=int(inp.readline())
array2=[int(i) for i in inp.readline().split()]
mainlist=array1+array2
sortedarr=mergeSort(mainlist)
for i in sortedarr:
    out.write(f'{i} ')
    
inp.close()
out.close()