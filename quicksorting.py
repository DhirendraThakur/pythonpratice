## 2nd way to do qucik sorting


def quick_sorting(data1):
    if len(data1) <= 1:
        return data1
    else:
        pivot_element = data1[0]
        left_hand_side = [x for x in data1[1: ] if x <= pivot_element]
        right_hand_side = [ x for x in data1[1: ] if x > pivot_element]
        
        return quick_sorting(left_hand_side)+ [pivot_element] + quick_sorting(right_hand_side)
    
    
my_list = [12, 15,2, 6, 26, 9, 32]

my_list = quick_sorting(my_list)
print(my_list)
