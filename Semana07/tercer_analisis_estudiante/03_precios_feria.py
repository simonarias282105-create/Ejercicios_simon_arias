"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
promedio = sum(precios) / len(precios)
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo

# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
tomate_supera_promedio = 0
i = 0

while i < len(precios):
    if precios[i] > promedio:
        tomate_supera_promedio += 1
    i += 1

# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    variacion = "Variación alta"
elif rango >= 150:
    variacion = "Variación moderada"
else:
    variacion = "Variación baja"

# TODO: Muestre producto y todos los resultados.
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
print(f"Producto: {producto}", 
      f"\nPromedio: ₡{promedio:.0f}", 
      f"\nMínimo: ₡{minimo:.0f}", 
      f"\nMáximo: ₡{maximo:.0f}", 
      f"\nRango: ₡{rango:.0f}", 
      f"\nCantidad de precios que superan el promedio: {tomate_supera_promedio}", 
      f"\nClasificación del rango: {variacion}")
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
