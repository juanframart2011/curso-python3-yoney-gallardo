#Tipos de cadena
cadena = 'Esto es una cadena'
print( type( cadena ) )

entero = 12345
print( type( entero ) )

flotante = 16.3
print( type( flotante ) )

boleano = True
print( type( boleano ) )

num_complejos = 7 + 4j
print( type( num_complejos ) )

#Aritmerico
uno = 11
dos = 3
print( uno % dos )

#Condicionales
uno = 10
dos = 10

if uno < dos: print( "Es menor" )
uno = uno - 1
if uno < dos: print( "Es menor" )

if uno < dos:
    print( "Es menor" )
elif uno == dos:
    print( "Son iguales" )
else:
    print( "Es diferente" )


#Arreglo
semana = ['Lunes','Martes','Miercoles','Jueves','Viernes']
if 'Martex' in semana:
    print("No se encontro")
else:
    print("otro día")
#Bucles
bucles = 1
while bucles < 10:
    print( "el valor es: ", bucles )
    bucles = bucles + 1

pr_text = "Hello World"
for i in pr_text:
    print( "Letras: ", i )

#Funciones
def saludo():
    print( "hola a todos" )

saludo()

def suma( p1, p2 ):
    print( p1 +  p2 )

suma( 1, 2 )

#Tuplas
tupley = ( 10, 20, 30, 40, "Running" )
print( tupley )
print( "Tupley 1", tupley[1] )

#Cadenas
name = "Lionel"
app = "Messi"
saludos = "Saludo: %s %s" %( name, app )
print( saludos )

saludos = "Saludo Format: {0}{1}" .format( name, app )
print( saludos )

#Listas
listas = ( 10, 20, 30, 40, "Running" )
