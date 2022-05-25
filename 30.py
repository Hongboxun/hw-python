end = False
ans="1234"
while end!=True:
    a=0
    b=0
    user=str(input ("輸入數字:"))
    for i in range(len(ans)):
        if ans[i]==user[i]:
            a+=1
        elif user[i] in ans:
            b+=1   
    if (a==4) :
            end = True
            print( a,"A", b,"B")
