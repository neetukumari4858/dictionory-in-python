l=[]
def div(a):
    i=0
    while i <len(a):
        if a[i]%3==0:
            l.append(a[i])
        i=i+1
    return(l)
k=div([15,60,9,30,35,27,45])
def div1():
    p=[]
    j=0
    while j<len(l):
        if l[j]%5==0:
            p.append(l[j])
        j=j+1
    print(p)
div1()

