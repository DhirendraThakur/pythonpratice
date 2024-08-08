## arranging number in ascending order

def bubblesort(array1):
    data_array  = len(array1)
    for i in range(data_array):
        
        swapped = False
    
        for j in range(0, data_array- i- 1):
            if array1[j] > array1[j+1]:
            
                array1[j], array1[j+1] = array1[j+1], array1[j]
                swapped = True
                
        if not swapped:
            break
array1 = [21, 1, 45, 2]
bubblesort(array1)
            
print(f"The required bubble sort is {array1}")
            
    
    