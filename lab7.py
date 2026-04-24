import random
import math
import numpy as np
import pandas as pd
def generate_data(n=18):
    data=[]
    data.append({"zone":1,"traffic":0,"air_quality":50,"energy":100})
    data.append({"zone":2,"traffic":90,"air_quality":250,"energy":450})
    data.append({"zone":3,"traffic":60,"air_quality":120,"energy":480})
    for i in range(4,n+1):
        record={"zone":i,"traffic":random.randint(0,100),"air_quality":random.randint(0,300),"energy":random.randint(0,500)}
        data.append(record)
    return data
def classify_zone(record):
    traffic=record["traffic"]
    aqi=record["air_quality"]
    energy=record["energy"]
    if aqi>200 or traffic>80:
        return "High Risk"
    elif energy>400:
        return "Energy Critical"
    elif traffic<30 and aqi<100:
        return "Safe Zone"
    else:
        return "Moderate"
def custom_sort(data,key):
    n=len(data)
    for i in range(n):
        for j in range(0,n-i-1):
            if data[j][key]>data[j+1][key]:
                data[j],data[j+1]=data[j+1],data[j]
    return data
def calculate_risk(record):
    score=(record["traffic"]*0.4+record["air_quality"]*0.4+record["energy"]*0.2)
    return math.sqrt(score)
def detect_patterns(df):
    threshold=df["risk_score"].mean()
    multi_risk=df[(df["risk_score"]>threshold)&(df["air_quality"]>150)]
    traffic_var=np.var(df["traffic"])
    clusters=[]
    current=[]
    for i in range(len(df)):
        if df.iloc[i]["risk_score"]>threshold:
            current.append(df.iloc[i]["zone"])
        else:
            if len(current)>=2:
                clusters.append(current)
            current=[]
    if len(current)>=2:
        clusters.append(current)
    return multi_risk,traffic_var,clusters
data=generate_data()
for d in data:
    d["category"]=classify_zone(d)
roll_number=23
if roll_number%3==0:
    random.shuffle(data)
else:
    data=custom_sort(data,"traffic")
for d in data:
    d["risk_score"]=calculate_risk(d)
df=pd.DataFrame(data)
mean_values=np.mean(df[["traffic","air_quality","energy"]])
sorted_by_risk=custom_sort(data.copy(),"risk_score")
top3=sorted_by_risk[-3:]
multi_risk,traffic_var,clusters=detect_patterns(df)
max_risk=df["risk_score"].max()
min_risk=df["risk_score"].min()
avg_risk=df["risk_score"].mean()
risk_tuple=(max_risk,avg_risk,min_risk)
if max_risk>20:
    decision="Critical Emergency"
elif avg_risk>15:
    decision="High Alert"
elif avg_risk>10:
    decision="Moderate Risk"
else:
    decision="City Stable"
print(df)
print(df[["zone","category"]])
print(top3)
print(risk_tuple)
print(traffic_var)
print(clusters)
print(decision)
print("A smart city is one that predicts risks early, balances resources efficiently, and maintains environmental stability.")