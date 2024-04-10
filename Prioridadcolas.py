## Daniel Aguilar - Iván Camargo - 10/04/2024

class Usuario:
    def __init__(self, nombre, edad, direccion, motivo, gravedad):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.motivo = motivo
        self.gravedad = gravedad
        self.prioridad = 0
        if self.edad <12:
            self.prioridad = 1
        elif self.edad > 65:
            self.prioridad = 2
        else:
            self.prioridad = 4
        self.prioridadReal = self.gravedad * self.prioridad

class Sistema():
    def menu():    
        print("¿Qué desea hacer?")
        print("1. Ingresar datos")
        print("2. Pasar siguiente solicitud")
        print("3. Mostrar la cola ")
        print("4. Salir ")


class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i].prioridadReal < self.listaMonticulo[i // 2].prioridadReal:
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
          if self.listaMonticulo[i].prioridadReal > self.listaMonticulo[hm].prioridadReal:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2].prioridadReal < self.listaMonticulo[i*2+1].prioridadReal:
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



enElMenu = True
miMonticulo = MonticuloBinario()
while enElMenu:
    print("-----------------------")
    Sistema.menu()
    opcion = input("Ingrese su opción: ")
    if opcion == "1":
       nombre=input("Nombre:")
       edad=int(input("edad:"))
       direccion=input("direccion:")
       motivo=input("motivo:")
       gravedad=int(input("gravedad:"))
       NuevoUsuario=Usuario(nombre,edad,direccion,motivo,gravedad)
       miMonticulo.insertar(NuevoUsuario)
       print("Este usuario sera atendido en la posicion: ",miMonticulo.listaMonticulo.index(NuevoUsuario))
       

    
    elif opcion == "2":
       if miMonticulo.tamanoActual>0: 
            print("Siguiente solicitud a ser atendida:")
            print("Nombre:", miMonticulo.listaMonticulo[1].nombre)
            print("Edad:", miMonticulo.listaMonticulo[1].edad)
            print("Direccion:", miMonticulo.listaMonticulo[1].direccion)
            print("Motivo:", miMonticulo.listaMonticulo[1].motivo)
            print("Gravedad:", miMonticulo.listaMonticulo[1].gravedad)
            miMonticulo.eliminarMin()
       else:
           print("No hay solicitudes pendientes.")
    elif opcion == "3":
        print("Cola de atención en este momento:")
        for i in range(1, miMonticulo.tamanoActual + 1):
            miMonticulo.listaMonticulo[i]
            print("Nombre:", miMonticulo.listaMonticulo[i].nombre)
            print("Edad:", miMonticulo.listaMonticulo[i].edad)
            print("Direccion:", miMonticulo.listaMonticulo[i].direccion)
            print("Motivo:", miMonticulo.listaMonticulo[i].motivo)
            print("Gravedad:", miMonticulo.listaMonticulo[i].gravedad)
    elif opcion == "4":
            enElMenu = False
    else:
        print("Opción inválida. Intente nuevamente.")
 