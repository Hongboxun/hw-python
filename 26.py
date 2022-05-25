x="end"
while True:
    a=str(input("檢測的字串(end結束):"))
    if a!=x:
        b=str(input("檢測的單一字元:"))
        print("字元",b,"出現次數為:",a.count(b))
    else:
        print("檢測結束")
    break
