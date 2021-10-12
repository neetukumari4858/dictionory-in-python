student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

sum=0
i=0
user=input("enter keys:-")
while i <len(student):
      if user=="id":
            sum=sum+student[i]["id"]
      else:
            sum=sum+student[i]["success"]
      i=i+1
print(sum)

                        

                       

                 
        


              
        


          

