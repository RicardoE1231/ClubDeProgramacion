#Club De Programación PYTHON

num_lim = 1 + int(input("Ingresa Un Numero limite:"))
print("Ejercio 1")
for i in range(num_lim):
    for j in range(i):
        print(" *", end="")
    print()        


num_lim = int(input("Ingresa Un Numero limite:"))
print("Ejercio 2")
for i in range(num_lim):
    for j in range(num_lim, i,-1):
        print(" *", end="")
    print()

num_lim = 1 + int(input("Ingresa Un Numero limite:"))
print("Ejercio 3")
for i in range(num_lim):
    for j in range(i):
        print(" *", end="")
    print() 
for i in range(num_lim):
    for j in range(num_lim, i,-1):
        print(" *", end="")
    print()     

num_lim = 1 + int(input("Ingresa Un Numero limite:"))
print("Ejercio 4")
for i in range(num_lim):
    for j in range(num_lim):
        print(" *", end="")
    print()

num_lim = 1 + int(input("Ingresa Un Numero limite:"))
print("Ejercio Extra") 
for i in range(num_lim):
    for j in range(num_lim, i,-1):
        print(" *", end="")
    if i<(num_lim-1) : print()
for i in range(num_lim):
    for j in range(i):
        print(" *", end="")
    print()    