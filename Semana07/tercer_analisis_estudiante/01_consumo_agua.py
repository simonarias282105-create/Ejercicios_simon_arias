"""Caso 1: cambio del consumo diario de agua. Complete el programa."""

consumos_litros = [120, 115, 108, 102, 96]

# TODO: Calcule el consumo total y el promedio diario.
total= sum(consumos_litros)
promedio= total / len(consumos_litros)/100

# TODO: Compare el primer día con el último: litros ahorrados y porcentaje
#       de reducción respecto al primer día.
ahorro = consumos_litros[0] - consumos_litros[-1]
reduccion = (ahorro / consumos_litros[0]) * 100

# TODO: Clasifique: >=15 % reducción alta; >0 % reducción moderada;
#       de lo contrario, sin reducción.
if reduccion >= 15:
    clasificacion = "Reducción alta"
elif reduccion > 0:
    clasificacion = "Reducción moderada"
else:
    clasificacion = "Sin reducción"

# TODO: Muestre los cinco resultados.
# Control: total 541 L; promedio 108,2 L; ahorro 24 L; reducción 20 %;
#          reducción alta.
print(f"Consumo total: {total} L", 
      f"\nPromedio diario: {promedio:.1f} L", 
      f"\nLitros ahorrados: {ahorro} L", 
      f"\nPorcentaje de reducción: {reduccion:.0f} %", 
      f"\nClasificación: {clasificacion}")
# Prueba: use temporalmente cinco consumos iguales. Debe indicar 0 % y
# "Sin reducción". Restaure la lista antes de entregar.
