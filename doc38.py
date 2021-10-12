k={'c1': 'Red', 'c2': "green", 'c3': None}
# {'c1': 'Red', 'c2': 'Green'}
# k.popitem()
# print(k)
d={}
for i ,j in k.items():
    if j==None:
        pass
    else:
        d[i]=j
print(d)
