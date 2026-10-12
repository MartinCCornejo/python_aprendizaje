###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###
print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
name = 'Martín'
city = 'Tucumán'
print(name)
print(city)

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(f"El tipo de dato de {a} es: {type(a)}")
print(f"El tipo de dato de {b} es: {type(b)}")
print(f"El tipo de dato de {c} es: {type(c)}")
print(f"El tipo de dato de {d} es: {type(d)}")
print(f"El tipo de dato de {e} es: {type(e)}")

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
cadena = "12345"
cadena_int = int(cadena)
print(int(cadena_int))
print(type(int(cadena_int)))

cadena_float = float(cadena_int)
print(cadena_float)
print(type((cadena_float)))

float_number = 3.99
print(int(float_number)) 

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = 'Martín'
age = 24
height = 1.79

print(f"Hola! Me llamo {name} y tengo {age} años, mido {height} metros")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


result = int(round(3.1416) / 2)
print(result)