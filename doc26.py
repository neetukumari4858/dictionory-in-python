d={'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# C1 C2 C3                                                                                                      
# 1 5 9                                                                                                         
# 2 6 10                                                                                                        
# 3 7 11
l=[]
for i in d:
    print(i,end="  ")
print()
for j in d.values():
    l.append(j)
#print(l)
p=0
while p<len(l):
    u=0
    while u<len(l[p]):
        print(l[u][p],end =" ")
        u=u+1
    print()
    p=p+1
    
     









    


