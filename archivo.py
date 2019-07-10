def creacion():
    archivo = open( 'texto.txt', 'w' )
    archivo.close()

def escribir():
    archivo = open( 'texto.txt', 'a' )
    archivo.write( 'Lionel Messi \n' )
    archivo.write( '32 años \n' )
    archivo.close()

escribir()

def lectura():
    archivo = open( 'texto.txt', 'r' )
    txt = archivo.readline()

    while txt!='':
        print( txt )
        txt = archivo.readline()
        
    archivo.close()

lectura()
