### get sum of natural number

def sum_natural(n):
    if (n == 0):
        return 0 #returning 0 because natural number donot contain 0
        print (n)
    return sum_natural(n-1) + n 

print ((f"The sum of natural number is {sum_natural(5)}"))



## Create list and display the data using recursion

def rec_list(list, index = 0):
    if(index == len(list)):
        return
    
    print(rec_list(index))
    rec_list(list, index +1)
    
useful_files = ["Hello", "how ", "are", "you", "doing"]

rec_list(useful_files)