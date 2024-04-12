## Daniel Aguilar - Iván Camargo - 10/04/2024

#Clase usuario, en donde se tipifica el perfil del solicitante al sistema. 

class Usuario:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad
        self.prioridad = 0
        if self.edad <12:
            for i in range(1,edad):
                self.prioridad = edad//i
            self.prioridad = edad
        elif self.edad > 65:
            for i in range(1,edad-65):
                if edad//i > 12:
                 self.prioridad = edad//i
        else:
            self.prioridad = edad

##Clase sistema, en donde se encuentra la llamada al menú y el método para obtener la lista del montículo ordenada a través de un Bubble Sort típico

class Sistema():
    def menu():    
        print("¿Qué desea hacer?")
        print("1. Ingresar datos")
        print("2. Pasar siguiente solicitud")
        print("3. Mostrar la cola ")
        print("4. Salir ")

    def listaOrdenada(listaDeUsuarios):

        listaOrdenada = []
        listaOrdenada.extend(listaDeUsuarios) 
        listaOrdenada.remove(0)

        n = len(listaOrdenada)
        for i in range(n-1):

            
            for j in range(0, n-i-1):

                
                if (listaOrdenada[j].gravedad > listaOrdenada[j + 1].gravedad) or ((listaOrdenada[j].gravedad == listaOrdenada[j + 1].gravedad) and 
                                                                                   listaOrdenada[j].prioridad > listaOrdenada[j + 1].prioridad):
                    
                    listaOrdenada[j], listaOrdenada[j + 1] = listaOrdenada[j + 1], listaOrdenada[j]

        return listaOrdenada     
                
                
##Montículo binario y sus funciones para manejar la prioridad dentro de la cola del sistema. 

class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if (self.listaMonticulo[i].gravedad < self.listaMonticulo[i // 2].gravedad) or ((self.listaMonticulo[i].gravedad == self.listaMonticulo[i // 2].gravedad) and 
                                                                                          self.listaMonticulo[i].prioridad < self.listaMonticulo[i // 2].prioridad):
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self,usuario):
      self.listaMonticulo.append(usuario)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if (self.listaMonticulo[i].gravedad > self.listaMonticulo[hm].gravedad) or ((self.listaMonticulo[i].gravedad == self.listaMonticulo[hm].gravedad) and
                                                                                      self.listaMonticulo[i].prioridad > self.listaMonticulo[hm].prioridad):
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if (self.listaMonticulo[i*2].gravedad < self.listaMonticulo[i*2+1].gravedad) or ((self.listaMonticulo[i*2].gravedad == self.listaMonticulo[i*2+1].gravedad) and 
                                                                                           self.listaMonticulo[i*2].prioridad < self.listaMonticulo[i*2+1].prioridad) :
              return i * 2
          else:
              return i * 2 + 1

    def eliminarMin(self):
      valorSacado = self.listaMonticulo[1]
      self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
      self.tamanoActual = self.tamanoActual - 1
      self.listaMonticulo.pop()
      self.infiltAbajo(1)
      return valorSacado

    def construirMonticulo(self,unaLista):
      i = len(unaLista) // 2
      self.tamanoActual = len(unaLista)
      self.listaMonticulo = [0] + unaLista[:]
      while (i > 0):
          self.infiltAbajo(i)
          i = i - 1


##Función para entrar al menú del sistema.

enElMenu = True
miMonticulo = MonticuloBinario()
while enElMenu:
    print("-----------------------")
    Sistema.menu()
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
       nombre=input("Nombre:")
       edad=int(input("Edad:"))
       direccion=input("Dirección:")
       motivo=input("Motivo:")
       gravedad=int(input("Gravedad:"))
       NuevoUsuario=Usuario(nombre,edad,direccion,motivo,gravedad)
       miMonticulo.insertar(NuevoUsuario)
       print("El usuario será atendido en la posición: ", Sistema.listaOrdenada(miMonticulo.listaMonticulo).index(NuevoUsuario)+1)
       

    
    elif opcion == "2":
       if miMonticulo.tamanoActual>0: 
            print("Siguiente solicitud a ser atendida:")
            siguienteElemento = miMonticulo.eliminarMin()
            print("Nombre:", siguienteElemento.nombre)
            print("Edad:", siguienteElemento.edad)
            print("Direccion:", siguienteElemento.direccion)
            print("Motivo:", siguienteElemento.motivo)
            print("Gravedad:", siguienteElemento.gravedad)
            if siguienteElemento.gravedad == 5:
                print("El caso requiere una unidad móvil motorizada. Baja gravedad")
            elif siguienteElemento.gravedad == 1:
                print("El caso requiere una patrulla y unidades de refuerzo. Gravedad máxima")

       
            
       else:
           print("No hay solicitudes pendientes.")
    elif opcion == "3":
        print("Cola de atención en este momento:")
        for i in range(0, miMonticulo.tamanoActual):
            elementoActual = Sistema.listaOrdenada(miMonticulo.listaMonticulo)[i]
            print("Nombre:", elementoActual.nombre)
            print("Edad:", elementoActual.edad)
            print("Direccion:", elementoActual.direccion)
            print("Motivo:", elementoActual.motivo)
            print("Gravedad:", elementoActual.gravedad)

    elif opcion == "4":
            enElMenu = False
    else:
        print("Opción inválida. Intente nuevamente.")

##Zona de Pruebas. Ignorar

"""
miMonticulo = MonticuloBinario()

listaPersonas = []

jaime = Usuario("jaime",10,"asofn","asofn",1)
madrid = Usuario("madrid",23,"asf","gf",2)
juanjo = Usuario("juanjose",70,"asf","gf",1)

listaPersonas.append(jaime)
listaPersonas.append(madrid)
listaPersonas.append(juanjo)

miMonticulo.construirMonticulo(listaPersonas)

print(miMonticulo.listaMonticulo[1].nombre)
print(miMonticulo.listaMonticulo[2].nombre)
print(miMonticulo.listaMonticulo[3].nombre)


print(miMonticulo.eliminarMin().nombre)
print(miMonticulo.eliminarMin().nombre)
print(miMonticulo.eliminarMin().nombre)

print(miMonticulo.listaMonticulo)
print(Sistema.listaOrdenada(miMonticulo.listaMonticulo)[0].nombre)
print(Sistema.listaOrdenada(miMonticulo.listaMonticulo)[1].nombre)
print(Sistema.listaOrdenada(miMonticulo.listaMonticulo)[2].nombre)
"""