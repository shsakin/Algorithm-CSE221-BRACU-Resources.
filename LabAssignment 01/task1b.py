inp=open("input1b.txt", "r")
out=open("output1b.txt", "w")
testcase=inp.readline()
for i in range(int(testcase)):
    newline='\n'
    line=inp.readline()
    line=line.split()
    if i==int(testcase)-1:
        newline=''
    if line[2]=='+':
        val=int(line[1])+int(line[3])
    elif line[2]=='-':
        val=int(line[1])-int(line[3])
    elif line[2]=='*':
        val=int(line[1])*int(line[3])
    elif line[2]=='/':
        val=int(line[1])/int(line[3])

    out.write(f'The result of {line[1]} {line[2]} {line[3]} is {val}{newline}')
inp.close()
out.close()