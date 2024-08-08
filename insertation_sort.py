##insertation sorting

def insertation_sort(array):
    ## start for loop from 2nd item of array until last 
    for i in range(1, len(array)):
        main_item = array[i]
        
        j = i-1
        
        while j >= 0 and array[j] > main_item:
            array[j+1] = array[j]
            j -= 1
            array[j+1] = main_item
            
    return array

get_insert = [12,56,7, 90.1, 55]
new_array= insertation_sort(get_insert)
print(f"insertation sort = {new_array}") 
            