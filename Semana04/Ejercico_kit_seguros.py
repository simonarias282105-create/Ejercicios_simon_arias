#Misión kit seguro
#Entrada de datos
nombre= input('nombre: ').upper().strip()
kit= input('Tipo de kit: ').lower().strip()
autorizacion= input('Tiene autorizacion (si/no): ').lower().strip()=='si'
try:
    cantidad= int(input('Cantidad de kits: '))
except valueError:
                print('Cantidad de kist inválida, digite del 1 al 100')
                cantidad==1
dias= int(input('Días de préstamo: '))              
                
try:dias= int(input('Cantidad de días: '))
except valueError:
    print('Cantidad de días inválida, digite del 1 al 100')
    dias= -1

if not nombre or not kit or cantidad<1 or dias<1:
    resultado= 'Registro rechazado, revise los datos ingresados'

elif autorizacion and cantidad<=3 and not dias>7:
    resultado= f'solicitud aprobada, {nombre}: {3} kit(s)'
    
else:
    resultado= 'solicitud enviada a revisión'
    
print(resultado)
    