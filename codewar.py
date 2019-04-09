def get_pins(observed):
    '''TODO: This is your job, detective!'''
    observed=map(int,list(observed))
    everyword=[]
    for x in observed:
        word=[x]
        if x%3 and x!=0:
            word.append(x+1)
        if (x-1)%3:
            word.append(x-1)
        if (x-3)>0:
            word.append(x-3)
        if (x+3)<10 and x!=0:
            word.append(x+3)
        if x==8:
            word.append(0)
        if x==0:
            word.append(8)
        everyword.append(word)
        print(everyword)
    for i in range(len(everyword)):
        everyword[i]=list(map(str,everyword[i]))
    result=[]
    res=''
    length=1
    for word in everyword:
        res+=word[0]
        length*=len(word)
    result.append(res)
    no=0
    while True:
        # print(result)
        if len(result)>=length:
            break
        for i in result[:]:
            for j in range(len(everyword[no])):
                if j >0:
                    newi=list(i)
                    newi[no]=everyword[no][j]
                    newi=''.join(newi)
                    result.append(newi)
                    # print(newi)
                # print(result)
        no+=1
        print(no)
    return result


print(get_pins('13'))