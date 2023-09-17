def max_tasks(Intervals):
    Intervals.sort(key=lambda x: x[1])
    cur_finish_time = float('-inf')
    chosen_intervals = []
    for cur_interval in Intervals:
        if cur_interval[0]>=cur_finish_time:
            chosen_intervals.append(cur_interval)
            cur_finish_time = cur_interval[1]

    return chosen_intervals


inp=open('input1.txt','r')
out=open('output1.txt','w')
n=int(inp.readline())
Intervals=[]
for i in range(n):
    start,end=map(int,inp.readline().split())
    Intervals.append((start,end))

Results=max_tasks(Intervals)
out.write(f'{len(Results)}\n')
newline_count=0
for interval in Results:
    if newline_count==len(Results)-1:
        newline=' '
    else:
        newline='\n'
    newline_count+=1
    out.write(f'{interval[0]} {interval[1]}{newline}')


inp.close()
out.close()

# used finish first greedy algorithm for this task, this algorithm priroritize the finish time
# so sorted the intervals according to their finish time with lamda function, only appended in the chosen interval
# if one task is finished properly so we got how many task is possible if we handle one task at a time. 