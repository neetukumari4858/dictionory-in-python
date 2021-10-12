x=["neha","hena","tina"]
y=[10,30,29]
d={}
for i in x:
    for j in y:
        d[i]=j
        y.remove(j)
        break
print(d)
