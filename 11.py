b=[]
a=str(input("輸入月及日:"))
a.split(" ")
b.append(a)
if(b[0]==1 and b[1]>=21 or b[0]==2 and b[1]<=18):
    print("Aquarius")
elif(b[0]==2 and b[1]>=19 or b[0]==3 and b[1]<=20):
    print("Pisces")    
elif(b[0]==3 and b[1]>=21 or b[0]==4 and b[1]<=20):
    print("Aries")
elif(b[0]==4 and b[1]>=21 or b[0]==5 and b[1]<=21):
    print("Taurus")
elif(b[0]==5 and b[1]>=22 or b[0]==6 and b[1]<=21):
    print("Gemini")
elif(b[0]==6 and b[1]>=22 or b[0]==7 and b[1]<=22):
    print("Cancer")
elif(b[0]==7 and b[1]>=23 or b[0]==8 and b[1]<=23):
    print("Leo")
elif(b[0]==8 and b[1]>=24 or b[0]==9 and b[1]<=23):
    print("Virgo")
elif(b[0]==9 and b[1]>=24 or b[0]==10 and b[1]<=23):
    print("Libra")
elif(b[0]==10 and b[1]>=24 or b[0]==11 and b[1]<=22):
    print("Scorpio")
elif(b[0]==11 and b[1]>=23 or b[0]==12 and b[1]<=21):
    print("Sagittarius")
elif(b[0]==12 and b[1]>=22 or b[0]==1 and b[1]<=20):
    print("Capricorn")