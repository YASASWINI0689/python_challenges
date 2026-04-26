import copy
def generate_data():
    return [{"id":1,"data":{"files":["a.txt","b.txt"],"usage":500}},{"id":2,"data":{"files":["c.txt"],"usage":300}}]
def replicate_data(original):
    assigned=original
    shallow=list(original)
    deep=copy.deepcopy(original)
    return assigned,shallow,deep
def modify_data(data,roll_number):
    for user in data:
        files=user["data"]["files"]
        if roll_number%2==0:
            files.append("new_file.txt")
        else:
            if len(files)>0:
                files.pop()
        user["data"]["usage"]+=100
def check_integrity(original,modified,deep_copy):
    leakage_count=0
    safe_count=0
    overlap_count=0
    for i in range(len(original)):
        if original[i]["data"]["files"]==modified[i]["data"]["files"]:
            leakage_count+=1
        if original[i]["data"]["files"]!=deep_copy[i]["data"]["files"]:
            safe_count+=1
        original_files=set(original[i]["data"]["files"])
        modified_files=set(modified[i]["data"]["files"])
        overlap=original_files.intersection(modified_files)
        overlap_count+=len(overlap)
    return (leakage_count,safe_count,overlap_count)
roll_number=22
original_data=generate_data()
assigned,shallow_copy,deep_copy=replicate_data(original_data)
print(original_data)
print(shallow_copy)
print(deep_copy)
modify_data(shallow_copy,roll_number)
print(original_data)
print(shallow_copy)
print(deep_copy)
report=check_integrity(original_data,shallow_copy,deep_copy)
print(report)