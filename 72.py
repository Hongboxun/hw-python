n=int(input("請輸入n:"))
k=int(input("請輸入k:"))
if (n>=k):
    print("Peter可以抽",n+(n//k),"菸")
elif(n<k):
    print("Peter可以抽",n,"菸")    