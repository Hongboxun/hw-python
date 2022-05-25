a=["red","blue","red","green"]
for i in range (10):
    b=input("依序輸入四個顏色(中間以空格隔開):")
    if(b=="red blue red green"):
        print("正確答案")
    elif(i==10):
        print("失敗")    
        break
    else:
        h=""
        d=b.split(" ")
        for t in range(4):
            if a[t]==d[t]:
              h+="1"
            elif a[t]!=d[t] and a.count(d[t])>0:
                h+="2"
            else:
                h+="3"
        print(h)



