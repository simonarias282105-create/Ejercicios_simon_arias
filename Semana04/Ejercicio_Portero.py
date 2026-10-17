"""Microreto: el potrero"""
#Simón Arias Giraldo

#Entrada de datos
nombre= input('Ingrese su nombre: ').upper().strip()
energia= int(input('Cuanta energía tienes de 0 a 100: '))
traecafe= input('Trae café (si/no):').lower().strip()=='si'

#Si tengo menos del 50% y no tengo café= descaso
#Si tengo 50% de energía o más o tengo café= puede ingresar a la clase
#otro escenario: potrero confundido: revisar respuestas
mensaje='Condiciones para ingresar'

#proceso de datos
if energia<50 and not(traecafe):
    mensaje='Acceso denegado, ve a descansar'
elif energia>50 or traecafe:
    mensaje='puede ingresar a la clase'
else:
    mensaje='portero confundido, revisar respuestas'
    
#salida de datos
print(f'{nombre}:{mensaje}')