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
    
#_____________
    
# Creating a different class
    
class SalesforceModel:
	#Class attribute
	platform= "Einstein"

	# __init__ definition | Initial object state
	def __init__(self, model_name):
	
		# Intstance attributes
		self.model_name = model_name
		self.is_trained = False
		self.score = None

		# Local variables
		temp_id = 99
	
		# Printing the local variable value
		print(f"The value of the temp_id is {temp_id}")

	def train(self):
		self.is_trained = True
		self.score = 0.85

	# static method

	@staticmethod
	def is_high_performance(score):
		if score > 0.8:
			return True
		else:
			return False

	# class method

	@classmethod
	def create_default(cls, name):
		return cls(model_name = name)    

#___ Inheritance ___

class EinsteinService:
	def __init__(self, service_id):
		self.service_id = service_id
	
class ChatbotService(EinsteinService):
	def __init__(self, service_id, language):
		super().__init__(service_id) #Esta línea de código es lo que hace que los valores del padre se ejecuten.
		self.language = language
		
	def status(self):
		print(f"Service {self.service_id} is running in {self.language}")

#___ Encapsulamiento ___

class SalesforceModelEncapsulado:
    def __init__(self, lr):
        self.__learning_rate = lr  # Atributo PRIVADO
        self.is_trained = False    # Atributo PÚBLICO

    def set_learning_rate(self, new_lr):
        """Puerta controlada para cambiar el dato"""
        if 0 < new_lr < 1:
            self.__learning_rate = new_lr
            print(f"LR actualizado a {new_lr}")
        else:
            print("Error: Valor de LR inválido")

    def get_lr(self):
        return self.__learning_rate

#_____________

# Creating the objects

if __name__ == "__main__":
    my_first_model = SalesforceModel(
        model_name= "model_test_1"
    )
    print(f"Model name: {my_first_model.model_name}")
    print(f"Type: {type(my_first_model)}")
    print(f"Is this model trained?: {my_first_model.is_trained}")
    print(f"Model score: {my_first_model.score}")

    print("\n")
    print("\n")

    print(f"Training the model...")
    my_first_model.train()
    my_first_model.score = 0.76
    print("Model Trained")

    print("\n")
    print("\n")

    print(f"Is this model trained?: {my_first_model.is_trained}")
    print(f"Model score: {my_first_model.score}")
    print(f"Is this high performance?: {SalesforceModel.is_high_performance(my_first_model.score)}")

    print("\n")
    print("\n")

    my_second_model = SalesforceModel.create_default(name="model_test_2")

    print(f"Model name: {my_second_model.model_name}")
    print(f"Type: {type(my_second_model)}")
    print(f"Is this model trained?: {my_second_model.is_trained}")
    print(f"Model score: {my_second_model.score}")

    print("\n")
    print("\n")

    print(f"Training the model...")
    my_second_model.train()
    my_second_model.score = 0.86
    print("Model Trained")

    print("\n")
    print("\n")

    print(f"Is this model trained?: {my_second_model.is_trained}")
    print(f"Model score: {my_second_model.score}")
    print(f"Is this high performance?: {SalesforceModel.is_high_performance(my_second_model.score)}")
    
    print("\n")
    print("\n")
    
    print("Inheritance")
    my_first_chatbit_service = ChatbotService(service_id="999", language="English")
    print(f"Service ID: {my_first_chatbit_service.service_id}")
    print(f"Language: {my_first_chatbit_service.language}")
    my_first_chatbit_service.status()
    print("\n")
    print("\n")