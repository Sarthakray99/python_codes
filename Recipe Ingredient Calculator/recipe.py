try:
    import re
    def parameter_calc():
        z = input("Enter the parameters for the recipe: ")
        N = int(input("Enter the no of people the recipe is for: "))
        ch1 = []
        ch = 'y'
        while ch == 'y':
            m,n = input("Enter ingredient and its quantity: ").split(',') # format - "ingredient,number quantity"
            y= []
            y = re.split(" ", n)
            y[0] = float(eval(y[0]))
            ch1.append((m, y[0]/N, y[1]))
            ch = input("choice: ")
        M = int(input("Enter the desired no of people for the recipe: "))
        print('')
        print(f"NOW FOR THE FINAL RECIPE FOR {z}")
        print('')
        for i in ch1:
            m = i[0]
            n,p = (i[1]*M).as_integer_ratio()
            o = i[2]
            if p != 1:
                a = n // p
                b = n % p
                print(f"{m}: {a} {b}/{p} {o}")
            else:
                print(f"{m}: {n} {o}")


    parameter_calc()

except SyntaxError:
    print("Check if you gave a space after comma inplace of the number")