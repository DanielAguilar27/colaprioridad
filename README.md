
# Colas con Prioridad

Quiz de Estructuras de Datos sobre la Implementación de una Cola con Prioridad en una situación real. 


## Authors

- [Iván Camargo - 2230033](https://github.com/popcorner893)
- [Daniel Aguilar - 2230034](https://github.com/DanielAguilar27)


## Análisis
Una cola de prioridad es aquella en donde los elementos ingresan con una 
determinada prioridad, y según esa prioridad salen de la cola.

Un ejemplo muy común es el sistema de asignación de prioridad de atención en una unidad de emergencia de la policía nacional, línea 123.

En este ejemplo, supondremos la creación de un sistema para atender las llamadas realizadas a la policía. Es posible realizar los siguientes métodos:

- Ingresar Llamada (Ingresa datos del solicitante y muestra la posición en que será atendido)
- Pasar siguiente solicitud (Muestra los datos de la siguiente solicitud en ser atendido y lo saca de la cola)
- Mostrar la cola (Muestra la cola de atención en ese momento)



## Implementación

Para implementar cada función propuesta, se trabajó con los métodos propuestos en el código tomado como referencia de "Montículos en Python". 

Por tanto, como primer paso se debieron acomodar los métodos del montículo binario para ser utilizados a partir de los atributos "gravedad" y "prioridad" de cada  usuario. En resumen, a medida que se organiza el montículo, las comparaciones se dan a partir de estos valores; primero, con base en la gravedad, y despues, de acuerdo a la prioridad de cada usuario.

Para mostrar la posición en la que será atendido, la clase Sistema cuenta con un método para organizar la lista de usuarios presentes en el montículo.

Pasar a la siguiente solicitud implica mostrar los datos del elemento sacado del montículo a partir del método eliminarMin. 

Por último, para mostrar la cola se recorre la lista de los usuarios ordenados de acuerdo a su prioridad y gravedad.