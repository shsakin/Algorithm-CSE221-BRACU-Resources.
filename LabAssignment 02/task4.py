def find_maximum_value(arr):
    if len(arr)<=1:
        return arr[0]
    if len(arr)==2:
        return max(arr[0],arr[1])
    else:
        mid=len(arr)//2
        a1=find_maximum_value(arr[:mid])
        a2=find_maximum_value(arr[mid:])
        return max(a1,a2)
    
inp=open('input4.txt','r')
out=open('output4.txt','w')
length=int(inp.readline())
array=list(map(int,(inp.readline().split())))
out.write(str(find_maximum_value(array)))

inp.close()
out.close()

#time complexity is O(log2n) for this code.