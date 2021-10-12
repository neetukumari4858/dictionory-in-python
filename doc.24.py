d=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#({'item1': 1150, 'item2': 300})
i=0
sum=0
k={}
while i<len(d):
    if d[i]['item']=='item1':
        sum+=d[i]['amount']
    elif d[i]['item']=='item2':
        k['item2']=d[i]['amount']
    i=i+1
    k['item1']=sum
print(k)

