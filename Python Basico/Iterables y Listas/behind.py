##Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
my_list=[]
counter=0  
while counter<5:
    num=int(input("Ingrese el numero que desee"))
    counter+=1
    my_list.append(num)
     
print("La lista original es ", my_list)
my_list[0], my_list[-1]= my_list[-1], my_list[0] 
print("La lista con el primer y ultimo elemento cambiados es ", my_list)
  