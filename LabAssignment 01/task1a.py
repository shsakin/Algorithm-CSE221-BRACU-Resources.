inp=open("input1a.txt", "r")
out=open("output1a.txt", "w")
testcase=inp.readline()

for i in range(int(testcase)):
    newline='\n'
    curr=inp.readline()
    if i==int(testcase)-1:
        newline=''
    if int(curr)%2==0:
        out.write(f'{int(curr)} is an Even number.{newline}')
    else:
        out.write(f'{int(curr)} is an Odd number.{newline}')

inp.close()
out.close()