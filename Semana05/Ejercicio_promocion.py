#Nos conviene la promoción ?
producto= ['Café', 5000, 20]
porcentaje_aumento= 20

#proceso de datos
descuento= producto[1]*15/100
precio_promocional= producto[1]-descuento
ingreso_actual= producto[1]*producto[2]
unidades_proyectadas= (producto[2]*porcentaje_aumento/100)+producto[2]
ingreso_promocion= (precio_promocional*unidades_proyectadas)-ingreso_actual
ingreso_proyectado= ingreso_promocion+ingreso_actual

if ingreso_proyectado > 0:
    recomendacion= 'Lanzar'
else:
    recomendacion= 'No lanzar'

#Salida de datos
print('ANÁLISIS DE PROMOCIÓN')
print("\n")
print(f'Producto:{producto[0]}\nPrecio actual:₡{producto[1]}\nUnidades actuales:{producto[2]}')
print(f'Ingreso actuasl:₡{ingreso_actual}\nDescuento:₡{descuento:,.0f}\nPrecio promocional:₡{precio_promocional:,.0f}')
print(f'Aumento esperado en ventas:{porcentaje_aumento}%\nUnidades proyectadas:{unidades_proyectadas:,.0f}')
print(f'Ingreso con promoción:₡{ingreso_proyectado:,.0f}\nDiferencia:₡{ingreso_promocion:,.0f}')
print("\n")
print(recomendacion)