d={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d1={}
# Dictionary in ascending order by value :  [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 
for i,j in sorted(d.items()):
        d1[i]=j
print(d1)

