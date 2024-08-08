## simple recurrison example

def get_sum (n):
    if n ==1:
        return 1
    return n + get_sum(n-1) ## calling get_sum its own defined function

print(get_sum(6))


## Fibonachi number example
## fibonachi means addition of 2 previous index number 

def fibo_number(num):
    if num==0 or num == 1:
        return num
    return fibo_number(num-1) + fibo_number(num-2)
print(f"The required number is {fibo_number(8)}")