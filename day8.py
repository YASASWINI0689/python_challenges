import random,math,copy,numpy as np,pandas as pd

def generate_data(n=15):
    return [{"zone":i+1,"metrics":{"traffic":random.randint(50,200),"pollution":random.randint(30,150),"energy":random.randint(40,180)},"history":[random.randint(20,100) for _ in range(5)]} for i in range(n)]

def personalize_data(data,roll):
    return list(reversed(data)) if roll%2==0 else data[3:]+data[:3]

def custom_risk_score(t,p,e):
    b=t+p+e
    return math.log(b+1)+math.sqrt(b)

def apply_risk(data):
    for d in data:
        m=d["metrics"]
        d["risk"]=custom_risk_score(m["traffic"],m["pollution"],m["energy"])

def mutate_data(data):
    for d in data:
        d["metrics"]["traffic"]+=20
        d["history"].append(random.randint(100,200))

def to_df(data):
    return pd.DataFrame([{"zone":d["zone"],"traffic":d["metrics"]["traffic"],"pollution":d["metrics"]["pollution"],"energy":d["metrics"]["energy"],"risk":d.get("risk",0)} for d in data])

def corr(x,y):
    mx,my=np.mean(x),np.mean(y)
    return np.sum((x-mx)*(y-my))/math.sqrt(np.sum((x-mx)**2)*np.sum((y-my)**2))

def analyze(df):
    m,v,s=df["risk"].mean(),df["risk"].var(),df["risk"].std()
    a=df[df["risk"]>m+s]["zone"].tolist()
    c=corr(df["traffic"].values,df["pollution"].values)
    return m,v,s,a,c

def clusters(z):
    res=[];t=[]
    for i in range(len(z)):
        if i==0 or z[i]==z[i-1]+1:t.append(z[i])
        else:res.append(t);t=[z[i]]
    if t:res.append(t)
    return res

def decision(v,a):
    return "System Stable" if v<10 else "Moderate Risk" if a<3 else "High Corruption Risk" if a<6 else "Critical Failure"

def main():
    roll=21
    original=personalize_data(generate_data(),roll)
    assign=original
    shallow=copy.copy(original)
    deep=copy.deepcopy(original)
    print(original[0])
    mutate_data(shallow)
    apply_risk(shallow)
    print(original[0])
    print(shallow[0])
    print(deep[0])
    df=to_df(original)
    print(df)
    m,v,s,a,c=analyze(df)
    print(m,v,c)
    print(a)
    cl=clusters(sorted(a))
    print(cl)
    si=1/(v+1)
    tup=(df["risk"].max(),df["risk"].min(),si)
    print(tup)
    print(decision(v,len(a)))

main()