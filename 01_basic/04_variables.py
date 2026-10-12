##
# 04 - Variables
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

my_name = "Martín"


age = 23

print(age)
print((type(age)))


age = "24"
print((type(age)))
print(my_name, age) 

# F-string 
print(f"Hola, mi nombre es {my_name} y tengo {age} años")

# No recomendada forma de asignar variables 
name, age, city = "Martin", 24, "Tucumán"

# Convenciones de nombres de variables
mi_nombre_de_variable = "ok"
nombre = "ok"

MiNombreDeVariable = "ko" # PascalCase
minombredevariable = "ko" # todojunto

mi_nombre_de_variable123 = "ok" 

MI_CONSTANTE = 3.13 # UPPER_CASE => constantes

# 1223123_variable = "ko"
# mi-variable = "ko"
# mi variable = "ko"

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

is_user_logged_in: bool = True
print(type(is_user_logged_in))

# is_user_logged_in = 21
print(type(is_user_logged_in))
