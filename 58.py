b=[]
for i in range (10):
    a=int(input("請輸入第i數字:"))
    b.append(a)
    b.sort()
print("最大的3個數為:",b[9],b[8],b[7])
print("最小的3個數為:",b[2],b[1],b[0])    