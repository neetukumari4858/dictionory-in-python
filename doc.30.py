
#New dictionary:  {'S001': ['Math', 'Science'], 'S002': ['Math', 'English']}

l={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
k=" "
d={}
for i in l:
     #print(i)
    str1=""
    for j in i:
        # print(j)
        if j!=k:
            str1+=j
    d[str1]=l[i]
print(d)
