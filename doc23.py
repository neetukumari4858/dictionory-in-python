my_dict = {'A': 67, 'B': 23, 'C': 45,'D': 56, 'E': 12, 'F': 69}
#{'F': 69, 'A': 67, 'D': 56} 
max=0
sec_max=0
third_max=0
d={}
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        a=i
d[a]=max
for j in my_dict:
    if my_dict[j]<max:
        if my_dict[j]>sec_max:
            sec_max=my_dict[j]
            b=j
d[b]=sec_max
for k in my_dict:
    if my_dict[k]<max:
        if my_dict[k]<sec_max:
            if my_dict[k]>third_max:
                third_max=my_dict[k]
                c=k

d[c]=third_max
print(d)
