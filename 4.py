x=float(input("輸入x座標點:"))
y=float(input("輸入y座標點:"))
a=(x**2+y**2)
if(x>0 and y>0):
      print("第1象限",",離原點距離為根號",a)
elif(x<0 and y>0):
      print("第2象限",",離原點距離為根號",a) 
elif(x<0 and y<0):
      print("第3象限",",離原點距離為根號",a)       
elif(x>0 and y<0):
      print("第4象限",",離原點距離為根號",a) 
elif(x==0 and y>0):
      print("在上半平面y軸上",",離原點距離為根號",a)
elif(x==0 and y<0):
      print("在下半平面y軸上",",離原點距離為根號",a)
elif(x>0 and y==0):
      print("在右半平面y軸上",",離原點距離為根號",a)
elif(x<0 and y==0):
      print("在左半平面y軸上",",離原點距離為根號",a)      
elif(x==0 and y==0):
      print("在原點上")                  