def frog_jump(n):
    global dp_memory
    if n<2:
        return  1
    if dp_memory[n]!=-1:
        return dp_memory[n]
    dp_memory[n] = frog_jump(n-1)+frog_jump(n-2)
    return dp_memory[n]

inp=open('input2.txt','r')
out=open('output2.txt','w')
steps=int(inp.readline())
dp_memory=[-1]*(steps+1)
ways= frog_jump(steps)

out.write(f'{ways}')

inp.close()
out.close()

# basically a fibonacci series recursive call, sum of the previous two numbers, for memorizing the recursive calls, updated and every time check the global list if the value is already calculated.