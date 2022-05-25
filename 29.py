a=str(input("甲方的數字"))
b=str(input("乙方的數字"))
1>5
for i in range(len(a)):
    if(a[i]>b[i]):
        print("贏")
    elif(a[i]==b[i]):
        print("和")
    elif(a[i]<b[i]):
        print("輸")        