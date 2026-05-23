# Integrante:   HILTER SÀNCHEZ
#  Revision y validacion de Bubble Sort
# Parte 4: Ordenamiento alfabetico de cadenas - Bubble Sort
import copy

nombres_original = ['Rodrigo', 'Mariana', 'Hilter', 'Becsy', 'Ana', 'Carlos']
nombres = copy.copy(nombres_original)

print(f"Lista antes de ordenar : {nombres}")

# Bubble Sort: comparacion lexicografica
n = len(nombres)

for i in range(n - 1):
    for j in range(n - i - 1):
        if nombres[j] > nombres[j + 1]:
            nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]

print(f"Lista despues de ordenar: {nombres}")

verificacion = sorted(nombres_original)

print(f"Verificacion con sorted : {verificacion}")
print(f"El resultado es correcto: {nombres == verificacion}")