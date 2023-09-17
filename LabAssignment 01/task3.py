def selectionSort(arr,reverse=False):
    for i in range(len(arr)):
        idx=i
        for j in range(i+1,len(arr)):
            if not reverse:
                if arr[j]<arr[idx]:
                    idx=j
            else:
                if arr[j]>arr[idx]:
                    idx=j
        if not reverse:            
            if arr[idx]<arr[i]:
                arr[i],arr[idx]=arr[idx],arr[i]
        else:
            if arr[idx]>arr[i]:
                arr[i],arr[idx]=arr[idx],arr[i]

    return arr


inp=open("input3.txt", "r")
out=open("output3.txt", "w")
testcase=int(inp.readline().strip())
id=inp.readline().split()
mark=inp.readline().split()
id_mark_dic={}
for i in range(testcase):
    if int(mark[i]) in id_mark_dic:
        id_mark_dic[int(mark[i])].append(int(id[i]))
    else:
        id_mark_dic[int(mark[i])]=[int(id[i])]
descented=selectionSort(list(id_mark_dic.keys()),reverse=True)
descented_dic={}
for i in descented:
    descented_dic[i]=id_mark_dic[i]

newlineCount=0
for key,value in descented_dic.items():
    selectionSort(value)
    for i in value:
        if newlineCount==(testcase-1):
            newline=''
        else:
            newline='\n'
        out.write(f'ID: {i} Mark: {key}{newline}')
        newlineCount+=1

inp.close()
out.close()
