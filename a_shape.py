## A shape printing format
def a_shape():
    for i in range(7):
        for j in range(5):
            if ((j==0 or j == 4) and i!= 0) or ((i ==0 or i == 3) and (j>0 and j <4)):
                print("A", end="")
            else:
                print(end=" ")
                
        print()
a_shape()