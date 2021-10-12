d={}
name=["megha","raghav","suman"]
marks=[40,34,55,23]
for i in name:
    for j in marks:
        d[i]=j 
        marks.remove(j)
        break
print(d)