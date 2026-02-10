name="Yasaswini"
n=int(input())
marks=[0]*n
for i in range(n):
    marks[i]=int(input())
v=0
f=0
for m in marks:
    if name[0]=='Y':
        m=m + 1
    if m<0 or m>100:
        print(m,"Invalid")
    else:
        v=v + 1
        if m>=90:
            print(m,"Excellent")
        elif m>=75:
            print(m,"Very Good")
        elif m>=60:
            print(m,"Good")
        elif m>=40:
            print(m,"Average")
        else:
            print(m,"Fail")
            f=f + 1
print("Valid:",v)
print("Fail:",f)
