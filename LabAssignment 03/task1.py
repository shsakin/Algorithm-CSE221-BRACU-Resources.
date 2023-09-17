def count_aliens(arr):
    if len(arr)<=1:
        return 0
    if len(arr)==2:
        return 1 if arr[0]>arr[1] else 0
    else:
        mid=len(arr)//2
        count_left=count_aliens(arr[:mid])
        count_right=count_aliens(arr[mid:])
        count_cross=cross_check(arr[:mid],arr[mid:])
        return (count_left+count_right+count_cross)
    
def cross_check(arr1,arr2):
    inv_count=0
    i,j=0,0
    while i<len(arr1):
        if j==len(arr2):
            j=0
            i+=1
        elif arr1[i]>arr2[j]:
            j+=1
            inv_count+=1
        else:
            j+=1
    return inv_count

inp=open('input1.txt','r')
out=open('output1.txt','w')
length=int(inp.readline())
array=[int(i) for i in inp.readline().split()]
out.write(str(count_aliens(array)))

inp.close()
out.close()