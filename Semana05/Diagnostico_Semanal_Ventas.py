"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro=640000
meta_norte=700000


# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro= sum(ventas_centro)
cantidad_centro= len(ventas_centro)
menor_centro= min(ventas_centro)
mayor_centro= max(ventas_centro)

# TODO: calcula promedio, rango, diferencia y porcentaje para Centro.
promedio_centro= total_centro/cantidad_centro
porcentaje_centro= total_centro*100/meta_centro



# TODO: repite los indicadores para Norte.
total_norte=sum(ventas_norte)
cantidad_norte=len(ventas_norte)
menor_norte= min(ventas_norte)
mayor_norte= max(ventas_norte)

promedio_norte= total_norte/cantidad_norte
porcentaje_norte= total_norte*100/meta_norte


# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
#Tienda centro
if total_centro>meta_centro:
    estado_centro='Meta superada'
elif total_centro==meta_centro:
    estado_centro='Meta alcanzada exactamente'
else:
    estado_centro='Meta no alcanzada'

#tienda norte
if total_norte>meta_norte:
    estado_norte='Meta superada'
elif total_norte==meta_norte:
    estado_norte='Meta alcanzada exactamente'
else:
    estado_norte='Meta no alcanzada'

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_ganadora= 'Tienda del centro'
elif total_norte > total_centro:
    tienda_ganadora= 'Tienda del norte'
else:
    tienda_ganadora='Las dos tiendas pasaron'
    
# TODO: presenta un reporte con etiquetas claras y f-strings.
print('\t\tComparacion de tiendas')
print("-"*70,"\n")

#tienda centro
print(f"Centro: total: {total_centro:,.1f} | meta: {meta_centro:,.2f} | cumplimiento: {porcentaje_centro:,.0f}")
print(f"centro logro: {estado_centro}")
print("-"*70,"\n")
#tienda norte
print(f"norte: total: {total_norte:,.1f} | meta: {meta_norte:,.2f} | cumplimiento: {porcentaje_norte:,.0f}")
print(f"norte logro: {estado_norte}")


# TODO: escribe las tres conclusiones solicitadas en la guía.
