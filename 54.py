def a(x):
    if (x<=1.5):
          print("所需車資為",75)
    else:
           print("所需車資為",round(75+((x-1.5)*5)))
               
while True:
   p=float(input("請輸入路程里程數(km):"))
   print(a(p))
   break