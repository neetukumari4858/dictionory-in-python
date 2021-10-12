d='w3resource'
dict={}
#Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
for i in d:
    c=0
    for j in d:
        if i==j:
            c=c+1
    dict[i]=c
print(dict)



