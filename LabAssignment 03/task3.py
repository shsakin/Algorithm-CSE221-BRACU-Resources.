def quick_Sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_Sort(arr,low,p-1)
        quick_Sort(arr,p+1,high)

def partition(arr,low,high):
    pivot=arr[low]
    i=low
    for j in range(i+1,high+1):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i],arr[low]=arr[low],arr[i]    #swapping with pivot
    return i

inp=open('input3.txt','r')
out=open('output3.txt','w')
length=int(inp.readline())
array=[int(i) for i in inp.readline().split()]
quick_Sort(array,0,len(array)-1)
for i in array:
    out.write(f'{i} ')

inp.close()
out.close()

