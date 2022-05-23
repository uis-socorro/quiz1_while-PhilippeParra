
# input
c1 = int(input("digite el capital de pedro: "))
c2 = int(input("digite el capital de juan: "))
c3 = int(input("digite el capital necesario para el negocio: "))
meses = 0

# processing

while c1 + c2 < c3:
    c1 = c1 * 1.03
    c2 = c2 + (c2 * 0.04)
    meses = meses + 1

# output


print("Los meses necesarios para que el capital de pedro y juan sirva para hacer su negocio son:")
print(meses , "meses.")