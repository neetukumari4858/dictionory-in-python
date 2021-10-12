d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
#[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
l=[]
for i in d.values():
    l.append(i)
print(l)
j=0
l1=[]
# print(l[0])
while j<len(l[0]):
    m=0
    dic={}
    for k in d:
        dic[k]=l[m][j]
        m+=1
    j+=1
    l1.append(dic)
print(l1)
    


  

    


