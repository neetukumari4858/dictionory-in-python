# d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# # Grouping a sequence of key-value pairs into a dictionary of lists:
# # {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
# i=0
# d1={}
# while i<len(d):
#     j=0
#     l=[]
#     while j<len(d[i]):
#         if (d[i][j])=="yellow":
#             k=d[i][j]
#         elif (d[i][j])=="blue":
#             k=d[i][j]
#         else:
#             l.append(d[i][j])
#         j=j+1
#         d1[k]=l
#     i=i+1
# d1[k]=l
# print(d1)



d=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
i=0
d1={}
k=[]
e=[]
a=[]
for i ,j in d:
    if i=="yellow":
        k.append(j)
        d1[i]=k
    elif i=="blue":
        e.append(j)
        d1[i]=e
    elif i =="red":
        a.append(j)
        d1[i]=a
print(d1)

