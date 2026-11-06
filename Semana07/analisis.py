from sedes import sedes

print("Sedes registradas: ", len(sedes))
print("Primera sede: ", sedes[0]["nombre"])
print("Ventas de la primera sede: ", sedes[0]["ventas"])

print("\nANALISIS DE EMPRENDIMIENTOS")

for sede in sedes:
    total= sum(sede["ventas"])
    porcentaje= (total / sede["meta"]) * 100

    #Clasificación de desempeño
    if porcentaje >= 100:
        estado= "Meta alcanzada"
    elif porcentaje >= 80:
        estado= "Meta casi alcanzada"
    else:
        estado= "Meta no alcanzada"

    print(
        f"{sede["nombre"]} | Total ventas: {total:,.2f} | "
        f"Porcentaje de meta: {porcentaje:.2f}% | Estado: {estado}"
    f"\n--------------------------------------------------------------------------------------------"
    )

