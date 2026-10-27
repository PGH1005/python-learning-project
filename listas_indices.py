#Indexado positivo, negativo y gestión del desbordamiento:

import plistlib
print(dir(plistlib))

ciudades = ["Bilbao", "Burgos", "Soria", "Teruel"]

print(ciudades[0])  # Bilbao
print(ciudades[-1])  # Teruel
print(ciudades[-3])  # Burgos

# Un índice fuera de rango lanza IndexError
try:
    print(ciudades[9])
except IndexError as error:
    print("Error controlado:", error)
# Error controlado: list index out of range

