d={"n":10,"m":20,"b":30}
max=0
i=0
l=[]
while i <len(d):
    if d[i]>max:
        max=d[i]
    i=i+1
print(max)
j=0
while j<=max:
    if j in d.values():
        l.append(j)
    j=j+1
print(l) 




 
 