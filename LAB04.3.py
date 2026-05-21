#Parte 3: Estructura combinada - lista de diccionarios
usuarios = [
    {"nombre": "Rodrigo Cabrera", "email": "rodrigo@upn.pe", "ciudad": "Cajamarca"},
    {"nombre": "Mariana Lezcano", "email": "mariana@upn.pe", "ciudad": "Lima"     },
    {"nombre": "Hilter Sanchez",  "email": "hilter@upn.pe",  "ciudad": "Cajamarca"},
    {"nombre": "Becsy Sandoval",  "email": "becsy@upn.pe",   "ciudad": "Trujillo" },
    {"nombre": "Ana Yopla",       "email": "ana@upn.pe",     "ciudad": "Cajamarca"},
    {"nombre": "Carlos Torres",   "email": "carlos@upn.pe",  "ciudad": "Lima"     },
]

print('=== Listado de usuarios ===')
for u in usuarios:
    print(f"  {u['nombre']:<22} | {u['email']:<25} | {u['ciudad']}")

ciudad = input("\nIngresa la ciudad a buscar: ")
print(f"\nUsuarios en {ciudad}:")
total = 0
for u in usuarios:
    if u['ciudad'].lower() == ciudad.lower():
        print(f"  -> {u['nombre']} | {u['email']}")
        total += 1
if total == 0:
    print("  No se encontraron usuarios en esa ciudad.")
print(f"  Total encontrado: {total} usuario(s).")