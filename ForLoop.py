colors=['red', 'blue','green', 'ornage']
for i in colors:
    print(i)

#Tuples    
point=(1,2,3)
for i in point:
    print(i)

#Lists    
names=['Aron','Akron','Vayu']
for i in names:
    print(i)
  
#Dictionaries    
ages={'Kevin':60, 'Bob':59}
for i in ages:
    print(i)
    
for i,j in ages.items():
    print(i,j)
 
#Strings    
for i in 'my_string':
    print(i)

#Multiples of 4    
count=1
while count<=26:
    if count%4==0:
        print(count)
    count+=1
 
#ForElse 
for i in ['red','blue']:
     if i=='yellow':
         print("it is yellow")
         break
else:
    print("yellow is not in the list")
  
#range
for i in range(10):
    print(i)
 
#uppercase colors    
colors=['red','yellow','blue','green']
uppercase_colors=[]
for i in colors:
    uppercase_colors.append(i.upper())
print(uppercase_colors)    
    
        