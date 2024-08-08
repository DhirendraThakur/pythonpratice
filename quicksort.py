## pick pivot point
## take start and end
## start = 0 + 1
## end = len(array) - 1


def swap_data(a, b, array):
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def get_quick_partation(datas, start, end):
    pivot_index = start
    pivot = datas [pivot_index]
    # start = pivot_index +1
    # end = pivot_index -1
    
    while start< end:
        while start < len(datas) and datas[start]<= pivot:
            start += 1
        while datas[end] > pivot:
            end -=1
        if start < end:
            swap_data(start, end, datas)
    swap_data(pivot_index, datas, end)
    return end
        
def quciksort(datas, start, end):
    if start < end:
        
       pi=get_quick_partation(start, end, datas)
       quciksort(datas, start, pi -1)
       quciksort(datas, pi- 1, end)
       
        


datas = [12,5, 67, 2, 7, 11, 29, 40]
quciksort(datas, 0, len(datas)-1)
print(datas)