def insertion_sort(arr):
    n = len(arr)                          # O(1) 
    for i in range(1, n):                 # O(n) 
        clave = arr[i]                    # O(n)
        j = i - 1                         # O(n)
        while j >= 0 and arr[j] > clave:  # O(n²)
            arr[j + 1] = arr[j]           # O(n²)
            j -= 1                        # O(n²)
        arr[j + 1] = clave                #  O(n)
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
	list_len = len(list_to_print)  #0(1)
	for index in range(min(list_len, 10)): #0(1)
		print(list_to_print[index])        #0(1)
		

################################################################### 

def generate_list_trios(list_a, list_b, list_c):
	result_list = []  #0(1)
	for element_a in list_a:# 0(n)
		for element_b in list_b:  #0(n²)
			for element_c in list_c:  #0(n³)
				result_list.append(f'{element_a} {element_b} {element_c}') #0(n³)
				
	return result_list  #0(1)