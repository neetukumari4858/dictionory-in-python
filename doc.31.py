my_dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
#Expected Output:
# item4 55
# item1 45.5
# item3 41.3
max=0
sec_max=0
third_max=0
d={}
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        a=i
print(a,max)
for j in my_dict:
    if my_dict[j]<max:
        if my_dict[j]>sec_max:
            sec_max=my_dict[j]
            b=j
print(b,sec_max)
for k in my_dict:
    if my_dict[k]<max:
        if my_dict[k]<sec_max:
            if my_dict[k]>third_max:
                third_max=my_dict[k]
                c=k
print(c,third_max)
