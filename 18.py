c={'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13}
a=str(input("輸入5個撲克牌點數:"))
b=a.split(" ")
p=c.get(b[0])
i=c.get(b[1])
m=c.get(b[2])
l=c.get(b[3])
o=c.get(b[4])
print(p+m+i+o+l)