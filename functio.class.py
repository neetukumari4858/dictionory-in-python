# def add(x,y):
#     z= x+y
#     return z
# def sub(a,b):
#     c=a+b
#     return (c+add(10,5))####this is change in 2 exp.
# v=sub(3,2)
# print(v)

##function use for call
def add(x,y):
    z= x+y
    return z
def sub(a,b):
    c=a+b+add(10,5)
    return (c)
v=sub(3,2)
print(v)


# ##variable use##
# def add(x,y):
#     z= x+y
#     return z
# h=add(10,5)
# def sub(a,b):
#     c=a+b+h
#     return (c)
# v=sub(3,2)
# print(v)


    


