while True:
    a=input("請輸入事項(若以無事項,請輸入end):")
    a.split(" ")
    b="end"
    if b!=a:
        s=range(len(a))
        for i in s:
            print(i+1,a[i])
    elif(b==a):
        break