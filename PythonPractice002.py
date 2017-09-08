
my_list = []
my_list.append(1) 
my_list.append(2) 
my_list2 = [55.55,"Hi",3,99,222,222]
my_list2[0]=333.333

#print (len(my_list),sum(my_list),my_list2.count(222))
#print (my_list2[0],my_list2[-1],my_list2[1:3],my_list2[2:])
#print (my_list2[2:3])

passwd={'Mars':00000,'Mark':56680}
passwd['Happy']=9999     
passwd['Smile']=123456

del passwd['Mars']
passwd['Mark']=passwd['Mark']+1

print (passwd)
print (passwd.keys())
print (passwd.get('Tony'))