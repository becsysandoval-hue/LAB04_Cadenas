# Parte 2: Listas paralelas - nombres y edades
nombres = ['Ana', 'Luis', 'Maria', 'Carlos', 'Lucia', 'Pedro']
edades  = [21,    19,     23,      20,        22,      18    ]

print('=== Listado de personas ===')
for i in range(len(nombres)):
    print(f"  {nombres[i]:<10} -> {edades[i]} años")

# Busqueda por nombre
nombre_buscar = input("\nIngresa el nombre a buscar: ")
encontrado = False
for i in range(len(nombres)):
    if nombres[i].lower() == nombre_buscar.lower():
        print(f"  {nombres[i]} tiene {edades[i]} años.")
        encontrado = True
        break
if not encontrado:
    print("  Ese nombre no esta en la lista.")