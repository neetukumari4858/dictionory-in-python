d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
#Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
d3={}
for i in d1:
    for j in d2:
        if i==j:
            d3[i]=d1[i]+d2[j]
           # break
        elif i not in d2:
            d3[i]=d1[i]
        elif j not in d1:
            d3[j]=d2[j]
print(d3)
