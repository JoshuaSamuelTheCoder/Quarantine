cnt=0
def divide(x):
    global cnt
    lst = []
    while(x>1):
        lst.append(x)
        if (x & 1==0):
            #Dividing even number by two by shifting binary digits one step to the right.
            x=x>>1
        else:
            a=x+1
            b=x-1
            #counters ac & bc will be used to count trailing 0s
            ac=bc=0
            #count trailing 0's for x+1
            while(a & 1==0):
                a=a>>1
                ac+=1
            #count trailing 0's for x-1
            while(b & 1==0):
                b=b>>1
                bc+=1
            #go with x+1 if it has more trailing 0s in binary format. Exception is number 3 as b10 can be divided in less steps than b100.
            #edge case 3 identified by manually testing numbers 1-10.
            if (ac>bc and x!=3):
                x+=1
            else:
                x-=1
        if x == 4 or x == 3:
            lst.append(2)

        cnt+=1

    return lst

def solution(n):
    global cnt
    n=int(n)
    return divide(n)
    #return cnt
