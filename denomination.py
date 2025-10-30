def denomination(a):
    
    Q = [1000, 500, 200, 100, 50, 20, 10]
    x = 0

    for i in range(7):
        q = Q[i]
        x = a // q 
        print("The Notes {} = {}".format(q,x))
        a = a % q

amount = int(input("Enter the amount here: "))
denomination(amount)

