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

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid=len(arr)//2
        a1=mergeSort(arr[:mid])
        a2=mergeSort(arr[mid:])
        return merge(a1,a2)
    
inp=open('input3.txt','r')
out=open('output3.txt','w')
length=int((inp.readline()))
array=[int(i) for i in inp.readline().split()]
for i in mergeSort(array):
    out.write(f'{i} ')

inp.close()
out.close()