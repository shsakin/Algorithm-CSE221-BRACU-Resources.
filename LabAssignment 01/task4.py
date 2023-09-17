def insertionSort(arr,idx,reverse=False):
    for i in range(1,len(arr)):
        count1=i
        count2=i-1
        while count2>=0:
            if not reverse:
                if arr[count1][idx]<arr[count2][idx]:
                        arr[count1],arr[count2] = arr[count2],arr[count1]
                        count1 -= 1
                        count2 -= 1
                else:
                    break

            else:
                if arr[count1][idx]>arr[count2][idx]:
                    arr[count1],arr[count2] = arr[count2],arr[count1]
                    count1 -= 1
                    count2 -= 1
                else:
                    break

inp=open('input4.txt','r')
out=open('output4.txt','w')
testcase=int(inp.readline())
name_location_time=[]
for i in range(testcase):
    info=inp.readline().split()
    time=info[6][:2]+info[6][3:]
    name_location_time.append([info[0],info[4],time])

insertionSort(name_location_time,2,reverse=True)
insertionSort(name_location_time,0)

for i in range(len(name_location_time)):
    if i==len(name_location_time)-1:
        newline=''
    else:
        newline='\n'
    out.write(f'{name_location_time[i][0]} will departure for {name_location_time[i][1]} at {name_location_time[i][2][:2]}:{name_location_time[i][2][2:]}{newline}')


inp.close()
out.close()
