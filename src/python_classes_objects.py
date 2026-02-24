#Una clase en python necesita un constsructor
#El constructor es lo primero que se va a ejecutar al mandar a instanciar la clase (crear el objeto).

class Person:
    # __init__ es un "Magic Method" (nombre reservado). Python lo busca automáticamente al crear una instancia.
    # No es una convención; si le cambias el nombre, deja de funcionar como constructor automático.
      # Es el nombre convencional para el constructor, el que inicializa el objeto. (El verdadero constructor es __new__ y se ejecuta automáricamente)
    # Existen muchos de estos "Magic Methods" o "Dunder Methods" (__dunder__). 
    # Su propósito es permitir que tus propios objetos interactúen con las funciones y operadores nativos de Python.
    
    def __init__(self, name, age): # Definición del constructor.
        
        # Asignamos la variable local 'name' al atributo de instancia 'self.name'.
        # Sin 'self', el valor se perdería al terminar el constructor y no podría usarse en otros métodos (como work).
        # Al hacer self.name = name, estás "pegando" ese valor al objeto (la instancia) que acabas de crear. De esta forma, el dato sobrevive y se queda guardado en la memoria del objeto para siempre.
        self.name = name
        self.age = age

    #Métodos
    #Una función dentro de la clase.
    def work(self):
        return f"{self.name} está trabajando duro"
    
    