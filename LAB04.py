# Parte 1: Metodos de manipulacion de cadenas
texto = "Fundamentos de Programacion en Python - UPN Cajamarca 2026"

# 1. Subcadena equivalente a Substring
subcadena = texto[0:24]
print("--- Metodos de cadenas ---")
print(f"Texto original       : {texto}")
print(f"Subcadena [0:24]     : {subcadena}")

# 2. Buscar con find() equivalente a IndexOf
pos = texto.find("Python")
print(f"Posicion de Python   : {pos}")

# 3. Reemplazar con replace()
nuevo_texto = texto.replace("Python", "C#")
print(f"Texto reemplazado    : {nuevo_texto}")

# 4. Separar con split()
palabras = texto.split()
print(f"Palabras separadas   : {palabras}")
print(f"Total de palabras    : {len(palabras)}")