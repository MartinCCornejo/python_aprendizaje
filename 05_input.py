###
# 05 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola.
###

name = input("Hola! Como te llamas?\n")
print(f"Encantado de conocerte {name}")

age = int(input(f'Cuantos años tienes {name}?\n'))

print("====================================")
print(f"Perfecto {name}, tienes {age} años y dentro de 20 años tendras {age + 20} años")
print("====================================")

country, city = input("En que pais y ciudad vives?\n").split()
print(f"Vives en {country}, ciudad {city}")