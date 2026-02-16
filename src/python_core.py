#___ Funciones ___
def hello_user(greet="Hola", name="Invitado"):
    print(f"{greet}, {name}")
    return
#___ args & kwargs

#*args [int,str,bool,...] -> Multiples valores como argumentos - Regresa una tupla
#**kwargs [key: value] -> Multiples valores como argumentos - Regresa un diccionario
#Se usan cuando no se tiene claro cuantos valores recibirá la función. 

#def fun1(*args,**kwargs)
#   print(args)
#   print(kwargs)

# print(fun1(1,2,3,4,5,num1=72, num2=73))
# (1,2,3,4,5) -> Tupla
# {'num1': 72, 'num2': 73} -> Diccionario

#En la lógica de la función se pueden iterar los valores y aplicar el resultado directamente en return.

def testing_args(*args, **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    return

#___ Higher Order function___

#Una función que recibe como parámetro una función o que regresa una función. 
#Este el principio de cómo funcionan los decoradores. 

#La función de orden superior
def require_auth(func): #Recibe la función como parámetro
    def wrapper(user): #Función anidada
        if user.lower() == "admin":
            return func(user) #Usa la función que ahora es global
        else:
            return "Acceso denegado"    
    return wrapper #Regresa la función anidada

def admin_dashboard(no_user): #no_user no tiene que coincidir con wrapper porque se evalua de manera posicional. 
    return f"Bienvenido al panel {no_user}"

auth_view_dashboard = require_auth(admin_dashboard)
#En este caso, se iguala la variable a la llamada de la función "require_auth".
#Esto regresa la función wrapper. Entonces, esto llamara la función wrapper. 

#___ Decoradores ___

#Es una forma de modificar el comportamiento de una función sin cambiar la función en sí misma.
#Recibe una función y retorna una función.
#El decorador evita que se defina una nueva variable donde se anidan las funciones. 
#En esencia, require_auth_d sigue siendo una función de orden superior. 

def require_auth_d(func): 
    def wrapper_d(user):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"    
    return wrapper_d 

@require_auth_d #auth_view_dashboard_d = require_auth_d(admin_dashboard_d)
def admin_dashboard_d(no_user):
    return f"Bienvenido al panel {no_user}"

#El decorador hace que se llame con la función anidada. Sin embargo, la lógica persiste en la función de orden superior. Lo que
#Puede volver confuso el concepto. Se sigue evaluando wrapper_d() & no hay un tipo especial en la llamada que diga que es decorador.
#Incluso el editor de VS Code no lo reconoce como decorador. 
#Sin embargo, el decorador se puede importar sin problema como función de un módulo. 

if __name__ == "__main__":
    #Funciones
    print("___Funciones___")
    hello_user()
    hello_user("Gus", "Bienvenido")
    hello_user(name="Gus", greet="Bienvenido")
    #args & kwargs
    print("___args & kwargs___")
    testing_args(1,2,3,4,5,num1=72, num2=73)
    #Higher order function
    print("___Higher order function___")
    print(auth_view_dashboard("admin")) #Esto básicamente ejecuta wrapper("admin") -> func(user) | La función que es global por require_auth. 
    print(auth_view_dashboard("invitado"))#Esto funciona porque los parámetros de wrapper & admin_dashboard se evaluan posicionalmente, no por match en el nombre. 
    #Decoradores
    print("___Decoradores___")
    print(admin_dashboard_d("admin"))
    print(admin_dashboard_d("invitado"))
    
    

