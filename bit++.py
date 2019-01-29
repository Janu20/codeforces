# codeforces
value=0
for _ in range(0,int(input())):
    x=str(input())
    plus=x.count("+")
    minus=x.count("-")
    if(plus==2):
        value+=1
    elif(minus==2):
        value-=1
print(value)
