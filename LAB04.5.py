# Parte 5 HILTER ALEXIS: Integracion - ordenamiento + busqueda textual

usuarios = [
    {"nombre": "Rodrigo Cabrera", "email": "rodrigo@upn.pe", "ciudad": "Cajamarca"},
    {"nombre": "Mariana Lezcano", "email": "mariana@upn.pe", "ciudad": "Lima"},
    {"nombre": "Hilter Sanchez", "email": "hilter@upn.pe", "ciudad": "Cajamarca"},
    {"nombre": "Becsy Sandoval", "email": "becsy@upn.pe", "ciudad": "Trujillo"},
    {"nombre": "Ana Yopla", "email": "ana@upn.pe", "ciudad": "Cajamarca"},
    {"nombre": "Carlos Torres", "email": "carlos@upn.pe", "ciudad": "Lima"},
]

# Ordenar por nombre con Bubble Sort
n = len(usuarios)

for i in range(n - 1):
    for j in range(n - i - 1):
        if usuarios[j]['nombre'] > usuarios[j+1]['nombre']:
            usuarios[j], usuarios[j+1] = usuarios[j+1], usuarios[j]

print('=== Usuarios ordenados alfabeticamente ===')

for u in usuarios:
    print(f" {u['nombre']:<22} | {u['ciudad']}")

kw = input("\nEscribe una palabra clave para buscar: ")

print(f"\nResultados para '{kw}' :")

resultados = [
    u for u in usuarios
    if kw.lower() in u['nombre'].lower()
    or kw.lower() in u['ciudad'].lower()
]

if resultados:
    for u in resultados:
        print(f" -> {u['nombre']} | {u['email']} | {u['ciudad']}")
else:
    print(" Sin resultados.")

print(f" Total: {len(resultados)} resultado(s).")