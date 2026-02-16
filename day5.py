name=input("Enter your full name: ")
count=0
for ch in name:
    if ch!=" ":
        count=count+1
pli=count%3
print("L value:",count)
print("PLI value:",pli)
data=input("Enter weights: ").split()
weights=[]
for item in data:
    weights=weights+[int(item)]
very_light=[];normal_load=[];heavy_load=[];overload=[];invalid=[]
for weight in weights:
    if weight<0:
        invalid=invalid+[weight]
    elif weight<=5:
        very_light=very_light+[weight]
    elif weight<=25:
        normal_load=normal_load+[weight]
    elif weight<=60:
        heavy_load=heavy_load+[weight]
    else:
        overload=overload+[weight]
valid=0
for weight in weights:
    if weight>=0:
        valid=valid+1
affected=0
if pli==0:
    print("Applied Rule A")
    for item in overload:
        invalid=invalid+[item]
        affected=affected+1
    overload=[]
elif pli==1:
    print("Applied Rule B")
    for item in very_light:
        affected=affected+1
    very_light=[]
else:
    print("Applied Rule C")
    for item in very_light:
        affected=affected+1
    for item in overload:
        affected=affected+1
    very_light=[];overload=[]
print("Total Valid:",valid)
print("Affected Items:",affected)
print("Very Light:",very_light)
print("Normal Load:",normal_load)
print("Heavy Load:",heavy_load)
print("Overload:",overload)
print("Invalid Entries:",invalid)