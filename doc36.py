d={'key1': 1, 'key2': 3, 'key3': 2}
d1={'key1': 1, 'key2': 2}
#Expected output: key1: 1 is present in both x and y
k={}
for i,j in d.items():
    u=i,j
    for x,y in d1.items():
        if x==i and y==j:
            k[i]=j
print(k)