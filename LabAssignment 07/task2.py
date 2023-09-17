def max_tasks_by_M(Intervals,M):
    Intervals.sort()
    work_done=0
    man_count=M
    for time,type in Intervals:
        if type==1:
            if man_count:
                work_done+=1
                man_count-=1
        else:
            if man_count<M:
                man_count+=1
    return work_done


inp=open('input2.txt','r')
out=open('output2.txt','w')
n, m = map(int, inp.readline().split())
Intervals = []
for i in range(n):
    start, end = map(int, inp.readline().split())
    Intervals.append((start,1))
    Intervals.append((end,0))

result=max_tasks_by_M(Intervals,m)
out.write(f'{result}')

inp.close()
out.close()


# created a custom interval to track start and end times, so with start time passed 1 and 0 for end times, so staring of the task decreamented the man count if there is man available,
# and when a task end we increase the man count, so we got maximum task possible with M peoples.



