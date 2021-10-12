
# m={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# #{'V': [], 'VI': [], 'VII': [2]}
# m1={}
# l=[]
# o=[]
# for i in m:
#     if i=='VII':
#         l.append(m[i][0])
#         m1[i]=l
#     else:
#         m1[i]=o
# print(m1)


d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
d1={}
for i in d:
    l=[]
    for j in d[i]:
        if j%2==0:
            l.append(j)
    d1[i]=l
print(d1)

  





