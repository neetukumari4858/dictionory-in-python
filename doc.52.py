d={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# ['f']
# ['f', 'i']
# ['f', 'i', 'g', 'd', 'c']
l=[]
s=[]

max=0
sec_max=0
third_max=0
fourth_max=0
fifth_max=0
for i in d:
    if d[i]>max:
        max=d[i]
        z=i
for j in d:
    if d[j]<max:
        if d[j]>sec_max or d[j]==sec_max:
            sec_max=d[j]
            y=j
#print(y)

for k in d:
    if d[k]<max:
        if d[k]<sec_max:
            if d[k]>third_max:
                third_max=d[k]
                e=k
for w in d:
    if d[w]<max:
        if d[w]<sec_max:
            if d[w]<third_max:
                if d[w]>fourth_max:
                    fourth_max=d[w]
                    b=w
for a in d:
    if d[a]<max:
        if d[a]<sec_max:
            if d[a]<third_max:
                if d[a]<fourth_max:
                    if d[a]>fifth_max:
                        fifth_max=d[a]
                        c=a
# l.append(z)
# v=z,y
# f=z,y,e,b,c
# print(l)
# print(v)
# print(list(f))
print(max,sec_max,third_max,fourth_max,fifth_max)