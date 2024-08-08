def star_main():
    n = 11
    for i in range(1, n):
            for j in range(0, n -i):
                print(end = ' ')
            for k in range(0, i):
                print('*', end= '.')
            print()    
star_main()