data=list(map(int,input().split()))
d={"efficient":[],"moderate":[],"high":[],"invalid":[]}
for i in data:
    if i<0:
        d["invalid"].append(i)
    elif i<=50:
        d["efficient"].append(i)
    elif i<=150:
        d["moderate"].append(i)
    else:
        d["high"].append(i)
valid=[i for i in data if i>=0]
total=sum(valid)
count=len(data)
t=(total,count)
if len(d["high"])>3:
    res="Overconsumption"
elif abs(len(d["efficient"])-len(d["moderate"]))<=1:
    res="Balanced Usage"
elif total>600:
    res="Energy Waste Detected"
elif len(d["high"])==0:
    res="Efficient Campus"
else:
    res="Moderate Usage"
print("efficient:",d["efficient"])
print("moderate:",d["moderate"])
print("high:",d["high"])
print("invalid:",d["invalid"])
print("total:",t[0])
print("buildings:",t[1])
print("result:",res)