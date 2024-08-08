def merging_aaray(array):
    if len(array) <= 1: 
        return array
    
    mid = len(array)//2 ## double divide gives integer answer, single give float
    left = array[:mid]
    right = array[mid:]
    merging_aaray(left)
    merging_aaray(right)
    return get_merge_array(left, right, array)

def get_merge_array(a,b, array):
    #sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i =j = k = 0
    
    while i< len_a and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            #sorted_list.append(a[i])
            i+= 1
            
        else:
            array[k] = b[j]
            #sorted_list.append(b[j])
            j += 1
        k += 1
            
    while i < len_a:
        array[k] = a[i]
       # sorted_list.append(a[i])
        i+=1
        k += 1
    while j < len_b:
        array[k] = b[j]
        j+=1
        k += 1
        #sorted_list.append(b[j])
    
    

# a= [12,2,55,77, 19,1]
# b = [3,4,16,5,89,10]
array = [12, 2, 55, 77, 19,1]

merging_aaray(array)
print(array)
#print(get_merge_array(a,b))
        