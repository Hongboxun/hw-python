a=int(input("輸入月租費型式:"))
b=int(input("輸入通話時間:"))
if(a==186):
    if(b*0.09<=2*a):
        print(b*0.09*0.9)
    else:
        print(b*0.09*0.8)  
elif(a==386):
    if(b*0.08<=2*a):
        print(b*0.08*0.8)
    else:
        print(round(b*0.08*0.7))   
elif(a==586):
    if(b*0.07<=2*a):
        print(b*0.07*0.7)
    else:
        print(b*0.07*0.6)    
elif(a==986):
    if(b*0.06<=2*a):
        print(b*0.06*0.6)
    else:
        print(b*0.06*0.5)                           