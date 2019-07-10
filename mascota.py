class mascota:

    def __init__( self, nombre, edad, altura ):
        
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def correr( self, primero ):
        
        return primero + " corriendo " + self.nombre

gato = mascota( "peke", 5, 20 )
print( gato.correr( "Vamos" ) )
