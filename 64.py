a=int(input("請輸入第一個要判斷的數字:"))
b=int(input("請輸入第二個要判斷的數字:"))
if (a>0):
   for i in range(2,a+1):
       if (a%2==0):
           print(a,"不是質數")
           break
   else:
        print(a,"是質數")
        
else:
   print(a,"不是質數")
if (b>0):
   for i in range(2,b+1):
       if (b%2==0):
           print(b,"不是質數")
           break
   else:
        print(b,"是質數")
else:
   print(b,"不是質數")
