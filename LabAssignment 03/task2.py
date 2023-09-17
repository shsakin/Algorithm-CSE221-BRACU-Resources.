def get_max(arr):
    n=len(arr)
    mid=n//2
    if n==1:
        return arr[0]
    if n==2:
        return (arr[0]+((arr[1])**2))
    left_max=get_max(arr[:mid])
    right_max=get_max(arr[mid:])
    cross_max=max(arr[:mid])+(cross(arr[mid:]))
    return (max(left_max,right_max,cross_max))

def cross(arr):
    maximum=arr[0]**2
    for i in range(len(arr)):
        if arr[i]**2>maximum:
            maximum=arr[i]**2
    return maximum

inp=open('input2.txt','r')
out=open('output2.txt','w')
length=int(inp.readline())
array=[int(i) for i in inp.readline().split()]
out.write(str(get_max(array)))

inp.close()
out.close()