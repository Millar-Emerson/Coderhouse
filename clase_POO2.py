#Crear una clase llamada Alumno
#Propiedades: nombre , dni , nota_uno , nota_dos
#Los datos de nota_uno y nota_dos no se tienen cuando se crea el alumno
#Crear un metodo que imprima todos los datos de los alumnos: get_datos
#Crear un metodo que setea la nota_uno: set_nota_uno
#Crear un metodo que muestre el estado del alumno/a: get_estado-->RECURSA(1,2,3),RECUPERA(4,5,6),APROBADO(7,8,9,10)

class alumno():
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
        self.nota_uno=None
        self.nota_dos=None
    
    
    def __str__(self):
        return f"Nombre:{self.nombre} Dni:{self.dni} Nota uno: {self.nota_uno} Nota Dos: {self.nota_dos}"
        
        
        
    def set_nota_uno(self, nota:int):
        if nota < 1 and nota>10:
            print("ingrese la nota de nuevo")
        else:
            self.nota_uno = nota
        
    def set_nota_dos(self,nota:int):
        if nota < 1 and nota>10:
            print("ingrese la nota de nuevo")
        else:
            self.nota_dos = nota

            
    def estado_alumno(self):
        if self.nota_uno+self.nota_dos/2 <= 3:
            print("recursa")
        elif self.nota_uno+self.nota_dos/2 <= 6:
            print("recupera")
        else:
            print("aprobado")
              
emerson=alumno("emerson","12233")
emerson.set_nota_uno(2)
emerson.set_nota_dos(8)

print(emerson)

emerson.estado_alumno()