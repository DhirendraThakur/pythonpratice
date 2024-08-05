def trying_somesample():
    
    array1 = [9, 5, 1, 6, 2, 0]
    sort_array = sorted(array1)
    print(f" Sorted list = {sort_array}")
    
trying_somesample()


# bubble sorting pratice

def bubble_sorting_pratice(array):
    len_array = len(array)
    
    for i in range(len_array):
        
        already_sorted = True
        for j in range(0, len_array-i- 1):
            
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j + 1], array[j]
                
                already_sorted = False
        if already_sorted:
            break
                     
    return array

array1 = [12,2,1,5,78,99,58]
new_sort = bubble_sorting_pratice(array1)
print(f"Result for bubble sort = {new_sort}")   