def find_kth_smallest(arr,low,high,k):
    p=partition(arr,low,high)
    if p+1==k:
        return arr[p]
    elif p+1<k:
        return find_kth_smallest(arr,p+1,high,k)
    else:
        return find_kth_smallest(arr,low,p-1,k)

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    for j in range(i+1,high+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[low]=arr[low],arr[i]
    return i

inp=open('input4.txt','r')
out=open('output4.txt','w')
length=int(inp.readline())
array=[int(i) for i in inp.readline().split()]
query=int(inp.readline())
for i in range(query):
    if i==query-1:
        newline=''
    else:
        newline='\n'
    k=int(inp.readline())
    out.write(f'{str(find_kth_smallest(array,0,(len(array)-1),k))}{newline}')

inp.close()
out.close()