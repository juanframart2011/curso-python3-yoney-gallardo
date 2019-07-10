uno = 'hola'
dos

try:
    print( dos )
    
except NameError:
    print( "Está mal" )

try:
    print( uno )
    
except NameError:
    print( "Está mal" )

else:
    print("todo esta bien")

try:
    print( uno )
    
except NameError:
    print( "Está mal" )

else:
    print("todo esta bien")
finally:
    print( "siempre se ejecuta" )
    
