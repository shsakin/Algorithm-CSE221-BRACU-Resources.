def coin_counter(amount,index,coins,n,coin_List,coin_count=0):
    if index>=n: 
        if amount==0: 
            coin_List.append(coin_count)
        return 
    if coins[index]<=amount:
        coin_counter(amount-coins[index],index,coins,n,coin_List,coin_count+1)
    coin_counter(amount,index+1,coins,n,coin_List,coin_count)
    
    return coin_List

inp=open('input3.txt','r')
out=open('output3.txt','w')
n,amount=map(int,inp.readline().split())
coins=[int(i) for i in inp.readline().split()]
coinList=[]
result= min(coin_counter(amount,0,coins,n,coinList))

out.write(f'{result}')

inp.close()
out.close()

# gone though the coin list, there are two recursive calls, once when a coin is consideres other when its not, when we consider we dont increase the index 
# but utherwise we do, when the remaining amount is zero, append in the coinlist, finally return the minimum of the coin list.