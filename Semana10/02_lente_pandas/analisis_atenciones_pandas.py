"""El mismo expediente, con Pandas y las mismas tres funciones."""

import pandas as pd
import atenciones
from pathlib import Path

ARCHIVO_CSV = Path(__file__).with_name("atenciones.csv")


def explorar_atenciones(atenciones):
   print('atenciones: ', len(atenciones))
   print('atenciones tipo:', type(atenciones))
   print('Campos: ', list(atenciones.columns))
   


def contar_categorias(atenciones):
    print('Medicamentos: ', atenciones['medicamento'].value_counts())
    print('Hospitales: ', atenciones['hospital'].value_counts())
    print('Diagnósticos: ', atenciones['diagnostico'].value_counts())


def concluir(atenciones):
    print('Personas: ', atenciones['cedula'].nunique())
    print('Minutos de espera: ', atenciones['minutos_espera'].sum())
    print('Promedio: ', atenciones['minutos_espera'].mean())


try:
    pass ##PANDAS.....
except FileNotFoundError:
    print(f"No encontramos el archivo: {ARCHIVO_CSV}")
    raise SystemExit(1)

if not atenciones.empty:
    explorar_atenciones(atenciones)
    contar_categorias(atenciones)
    concluir(atenciones)
else:
    print("El archivo no contiene atenciones.")
