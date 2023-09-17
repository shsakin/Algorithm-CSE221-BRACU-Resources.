def binary_search(sorted_list,key):
    low=0
    high=len(sorted_list)-1
    while low<=high:
        mid=(low+high)//2
        if sorted_list[mid]==key:
            return mid
        elif sorted_list[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1

inp=open('input1b.txt','r')
out=open('output1b.txt','w')
len_int=[int(i) for i in inp.readline().split()]
key=len_int[1]
array=[int(i) for i in inp.readline().split()]
sorted_array=sorted(array)
v1,v2=0,0
for i in range(len_int[0]):
    result=binary_search(sorted_array[i+1:],key-sorted_array[i])
    if result!=-1:
        v1=i
        v2=result+i+1
        values=sorted([str(array.index(sorted_array[v1])+1),str(array.index(sorted_array[v2])+1)])
        out.write(" ".join(values))
        break
if result==-1:
    out.write("IMPOSSIBLE")

inp.close()
out.close()
