d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
n=int(input("enter no:-"))
k={}
for i in d:
    if d[i]>n:
        k[i]=d[i]
print(k)



