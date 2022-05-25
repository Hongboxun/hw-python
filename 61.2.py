def a(t):
    m,s = t.strip().split(":")
    return int(m) * 60 + int(s)
while True:
  x=str(input("請輸入遊戲時間:"))
  c=(a(x)-75)//30+1
  b=c//2
  v=c//3
  n=c-v
  print(7*v+6*n-b,"隻兵")