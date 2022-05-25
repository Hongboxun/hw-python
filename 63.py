def x(p):  
    sum = 0  
    for i in range(1, p+1):  
        if p % i == 0:  
            sum+=i  
    if (p==sum-p):    
            print("perfect")
    elif(p>sum-p):    
            print("deficient")
    else:    
            print("abundant")   
    return p    
while True:
    a=int(input("請輸入正整數n:"))
    print(x(a))
    break