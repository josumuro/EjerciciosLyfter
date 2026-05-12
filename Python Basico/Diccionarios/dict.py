##Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus value

list_a=['name','rol','age']
list_b=['Josue','Developer',30]
result_dict = {}
for index in range(len(list_a)):
    key= list_a[index]
    value= list_b[index]
    result_dict[key]=value
print(result_dict)
    