a=int(input("輸入n值:"))
p=[]
for i in range (a):
   b=str(input("請輸入姓名:"))
   c=str(input("請輸入電子郵件:")) 
   p.append(b)
   p.append(c)
d=str(input("請輸入要查詢電子郵件的姓名:")) 
print(d,"電子郵件帳號為",p[a])
   
