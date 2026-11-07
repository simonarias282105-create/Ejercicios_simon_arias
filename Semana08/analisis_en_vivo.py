"""Semana 8: informe de atenciones hospitalarias ficticias.

Complete las fases con el docente. La lectura de datos ya está preparada.
"""

# FASE 0: CONSUMIR LA CONEXIÓN PREPARADA
# conexion_api.py se encuentra junto a este archivo.
from conexion_api import cargar_datos

registros = cargar_datos()
print("Fuente: JSON público de GitHub")
print("Atenciones recibidas:", len(registros))


# La muestra solicitada usa range(3): deben existir las posiciones 0, 1 y 2.
if len(registros) < 3:
    raise SystemExit("Se necesitan al menos 3 registros. Publique la etapa 3.")


# FASE 1: MOSTRAR Y CONTAR LOS MEDICAMENTOS DE TRES ATENCIONES
# FASE 2: CONTAR LOS MEDICAMENTOS DE TODAS LAS ATENCIONES

equivalencias = {
    "acetaminofén": "acetaminofen",
    "paracetamol": "acetaminofen",
    "antiácido": "antiacido",
    "losartán": "losartan",
}
conteo_medicamentos = {}
total_medicamentos = 0

print("\nAnalisis fase #1")
for indice in range (len(registros)):
    registro = registros[indice]
    print('\n\t\tInformación del paciente')
    print('Nombre del paciente:',registro['paciente_nombre'])
    print('Cédula del paciente:',registro['paciente_cedula'])
    print('medicamentos:',registro['medicamentos'])

    for medicamento in registro['medicamentos']:
        #Limpieza de los datos
        medicamento = medicamento.strip().lower()
        if medicamento in equivalencias:
            medicamento = equivalencias[medicamento]

        #Conteo de medicamentos
        total_medicamentos +=1
        if medicamento in conteo_medicamentos:
            conteo_medicamentos[medicamento] += 1
        else:
            conteo_medicamentos[medicamento] = 1

print("\n", total_medicamentos, "medicamentos en total")
for medicamento, cantidad in conteo_medicamentos.items():
    print(f"-{medicamento}: \t{cantidad}")


# FASE 3: CONTAR ATENCIONES POR HOSPITAL
conteo_hospital= {}
total_pacientes = 0
for registro in registros:
    hospital = registro['hospital'].strip().lower()
    total_pacientes += 1
    if hospital in conteo_hospital:
        conteo_hospital[hospital] += 1
    else:
        conteo_hospital[hospital] = 1

print(f"\nTotal de pacientes: {total_pacientes}")
print("Atenciones por hospital:")
for hospital, cantidad in conteo_hospital.items():
    print(f"-{hospital}: \t{cantidad}")


# FASE 4: CONTAR ATENCIONES POR ENFERMEDAD DIAGNOSTICADA
conteo_enfermedad= {}
total_enfermedades = 0
for registro in registros:
    enfermedad = registro['diagnostico'].strip().lower()
    total_enfermedades += 1
    if enfermedad in conteo_enfermedad:
        conteo_enfermedad[enfermedad] += 1
    else:
        conteo_enfermedad[enfermedad] = 1

print(f"\nTotal de enfermedades diagnosticadas: {total_enfermedades}")
print("Atenciones por enfermedad diagnosticada:")
for enfermedad, cantidad in conteo_enfermedad.items():
    print(f"-{enfermedad}: {cantidad}")


