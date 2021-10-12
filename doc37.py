d={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
# 15
# 25
# 35
# k=0
user=int(input("enter no:-"))
for i in d.values():
    c=1
    for j in i:
        #print(j)
        if c==user:
            print(j)
        c+=1
            
    
    
        