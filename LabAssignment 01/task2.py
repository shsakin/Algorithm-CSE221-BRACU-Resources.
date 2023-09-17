def bubblesort(arr):
    swap=False
    for i in range(len(arr)-1):                                 
            if i==0 or swap:                   #using a flag statement and checking whether the swapping is occuring in the inner loop or not, if swap is not happening that means the part is already sorted so, breaking the loop, so the best case scenario time complexity will be O(n).
                for j in range(len(arr)-i-1):                        
                    if arr[j]>arr[j+1]:
                        swap=True
                        arr[j],arr[j+1]=arr[j+1],arr[j]
            else:
                break

inp=open("input2.txt","r")
out=open("output2.txt","w")
length=inp.readline()
arr=list(map(int,(inp.readline().split())))
bubblesort(arr)
for i in arr:
    out.write(f'{i} ')

inp.close()
out.close()