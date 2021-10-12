d=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
#{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5: ['Zachary Simon', 'VII']}
i=0
l=[]
d1={}
while i<len(d):
    j=0
    l1=[]
    while j<len(d[i]):
        if d[i][j]==d[i][0]:
            pass
        else:
            l1.append(d[i][j])
        j=j+1
    d1[d[i][0]]=l1
    i=i+1
print(d1)
