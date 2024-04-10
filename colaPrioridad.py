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


class MonticuloBinario:
    def __init__(self):
        self.listaMonticulo = [0]
        self.tamanoActual = 0


    def infiltArriba(self,i):
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self,k):
      self.listaMonticulo.append(k)
      self.tamanoActual = self.tamanoActual + 1
      self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self,i):
      while (i * 2) <= self.tamanoActual:
          hm = self.hijoMin(i)
          if self.listaMonticulo[i] > self.listaMonticulo[hm]:
              tmp = self.listaMonticulo[i]
              self.listaMonticulo[i] = self.listaMonticulo[hm]
              self.listaMonticulo[hm] = tmp
          i = hm

    def hijoMin(self,i):
      if i * 2 + 1 > self.tamanoActual:
          return i * 2
      else:
          if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
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

miMonticulo = MonticuloBinario()
miMonticulo.construirMonticulo([9,5,6,2,3])

jaime = Usuario("jaime",11,"xd","dsad",3)
jaime2 = Usuario("jaime2",23,"xafadd","dsad",4)
jaime3 = Usuario("jaime3",66,"asf","dsad",1)

listaUsuarios = []

listaUsuarios.append(jaime)
listaUsuarios.append(jaime2)
listaUsuarios.append(jaime3)

print(listaUsuarios)

listaPrioridad = []
i = 0
while i < len(listaUsuarios):
    listaPrioridad.append(listaUsuarios[i].prioridadReal)
    i++

print(listaPrioridad)

"""
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
"""

"""enElMenu = True
while enElMenu:
    print("¿Qué desea hacer?")
    print("1. Ingresar datos")
    print("2. Pasar siguiente solicitud")
    print("3. Mostrar la cola ")
    print("4. Salir ")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
       print("xd")
    elif opcion == "2":
        print("asbfas")
    elif opcion == "3":
        print("asibfiaxnf")
    elif opcion == "4":
            enElMenu = False
    else:
        print("Opción inválida. Intente nuevamente.")"""
