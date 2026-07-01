def bubble_sort(arr):
    n = len(arr)                          # O(1)
    for i in range(n):                    # O(n)
        for j in range(0, n - i - 1):     # O(n²)
            if arr[j] > arr[j + 1]:       # O(n²)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(n²)
    return arr                            # O(1)

            

################################################################

def print_numbers_times_2(numbers_list):    # 0(1)
	for number in numbers_list:             #0(n)
		print(number * 2)                   #0(n)
            
#################################################################

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a:   #0(n)
		for element_b in list_b: #0(n²)
			if element_a == element_b: #0(n²)
				return True  #0(1)
				
	return False #0(1)


###################################################################
def print_10_or_less_elements(list_to_print):
    list_len = len(list_to_print)           # O(1) — len() es acceso directo, no recorre la lista
    for index in range(min(list_len, 10)):  # O(1) — el loop corre MÁXIMO 10 veces sin importar
                                            #        el tamaño de list_to_print.
                                            #        pone un techo fijo, no crece con el input, por eso seun el análisis de complejidad es O(1)
        print(list_to_print[index])         # O(1) — hereda el O(1) del loop que la contiene



################################################################### 

def generate_list_trios(list_a, list_b, list_c):
	result_list = []  #0(1)
	for element_a in list_a:# 0(n)
		for element_b in list_b:  #0(n²)
			for element_c in list_c:  #0(n³)
				result_list.append(f'{element_a} {element_b} {element_c}') #0(n³)
				
	return result_list  #0(1)