#Tenemos una lista de Caballeros del Zodiaco (nombre, dios al que apoya, y una armadura, signo del zodiaco). 
# De cada armadura sabemos que tienen nombre, material (bronce, plata, oro). 
# Requerimos lo siguiente:
#Mostrar todas las armaduras de los caballeros que apoyen a Atena.
#Mostrar los nombres de todos los dioses, sin repetidos.
#Mostrar a todos los signos del zodiaco que empiecen con la letra C.


class Caballero:
    #hacemos el constructor del caballero del zodiaco
    def __init__(self,nombre,dios,armadura):
        self.nombre=nombre
        self.dios=dios
        self.armadura=armadura
        
    def mostrar_armadura(self):
        #mostramos el dios y la armadura
        return f"Dios: {self.dios} Nombre Armadura: {self.armadura.nombre} Material armadura: {self.armadura.material}"
    
    def seguidor_dios(self,dios):
        #el return puede contener condicionales, por eso el "==". Toma el dios actual de la lista
        # y compara el dios que introducimos en el codigo. Si es true hace el return, sino no
        return self.dios==dios
    
    def obtener_dioses(caballeros):
        #set(...): Esto convierte la lista resultante de los nombres de los dioses en un conjunto. 
        # Como los conjuntos en Python no contienen elementos duplicados, 
        # esto asegura que solo se retengan los nombres de los dioses únicos.
        return set(caballero.dios for caballero in caballeros)
        
class Armadura:
    #hacemos el constructor de la armadura
    def __init__(self,nombre,material,signo):
        self.nombre=nombre
        self.material=material
        self.signo=signo
        
    def empieza_con(self, letra):
        #el metodo startswith() retorna True si el string comienza con el valor especifico, sino False
        return self.signo.startswith(letra)   
    
    
    
#Creamos una lista de caballeros con sus respectivas armaduras
caballeros=[
    Caballero("Seiya","Atena", Armadura("Pegaso","Bronce","Capricornio")),
    Caballero("Shiryu", "Atena", Armadura("Dragon", "Bronce","Cancer")),
    Caballero("Milo", "Ares", Armadura("Escorpio", "Oro","Sagitario"))
]


print("Armadura de todos los caballeros que apoyan a atena")
#recorre la lista de caballeros
for caballero in caballeros:
    if caballero.seguidor_dios("Atena"):
        print(caballero.mostrar_armadura())
        
print("Nombres de todos los dioses:")
#a la lista dioses le seteamos los dioses con el metodo set
dioses = Caballero.obtener_dioses(caballeros)
#recorremos la lista dioses
for dios in dioses:
    print(dios)
    
    
print ("signo del zodiaco que empieza con C")
#declaramos la lista signo_c con el metodo set
signo_c=set()
for caballero in caballeros:
    #hacemos un if con el metodo empieza_con dando una letra
    if caballero.armadura.empieza_con("C"):
        #añadimos los signos si el if se cumple con el metodo add
        signo_c.add(caballero.armadura.signo)
for signo in signo_c:
    #recorremos la lista signo
    print(signo)