d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
dic={}
i=0
l=[]
while i <len(d):
    for j in d[i]:
        if d[i][j] not in l:
            l.append(d[i][j] )
    i=i+1
print(l)

