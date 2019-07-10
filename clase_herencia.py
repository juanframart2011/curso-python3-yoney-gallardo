class uno():

    def accion( self ):
        print( "One part" )

class dos():

    def accion( self ):
        print( "Two part" )


def funcion( polimorfismo ):
    polimorfismo.accion()

ej1 = uno()
ej2 = dos()

funcion( ej1 )
