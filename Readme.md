# README #

# VirtualDiskGII #

## Justificación ##

Una de las peticiones más concurrentes entre alumnos de tercero y cuarto curso del grado de ingeniería informática es la de documentación de una especialidad diferente a la que estás cursando. Queramos o no, son muchas las ocasiones en las que las menciones se entrelazan, siendo necesario tener conocimientos de unas para elaborar trabajos de calidad en otras.

En primer y segundo curso es habitual el uso de una carpeta en dropbox para compartir todo tipo de información, convirtiéndose en un servidor de experiencias de años anteriores donde algunos aportan y todos consumen. En primero, el que aporta lo hace de buena fé, sin poner en cuestión el feedback de sus aportaciones. En segundo, la situación es similar, pero ya los aportadores empiezan a balancear lo aportado frente a lo recibido, balance que suele salir negativo y que provoca el abandono de dicha actividad aportadora.

En tercero y cuarto, el celo por lo propio es el gran dominante. Es muy complicado encontrar a alguien dispuesto a compartir. O por lo menos gratuitamente. Si deseas información, debes pagar con información. 

Y es en esta situación donde hemos puesto nuestro punto de mira. La pregunta es: ¿Qué podemos ofrecer a los alumnos de tercero y cuarto que facilite el intercambio de información?

La respuesta es clara. Deberíamos ofrecer a los alumnos un sistema cliente-servidor. Dicho sistema debe permitir a un usuario ofrecer sus ficheros a los demás a través de la red de la UCA. Pero, para poder salvaguardar el celo existente, el que ofrece los ficheros debe poder controlar quiénes acceden al mismo.

## Objetivo. ##

Proveer de una solucion para que las personas autorizadas a acceder a un servidor puedan intercambiar ficheros.

## Ubicación de los ficheros. ##

* Código fuente: Carpeta raíz.
* Documentación: Carpeta ./docs

## Instalacion y Funcionamiento ##

**Ejecución del servidor**

En el directorio donde ejecutemos el servidor deberá contener una carpeta denominada **Compartir**. Si deseamos autorizar a un usuario, deberemos hacerlo en la estructura para tal fin existente en el código. En Linux, para ejecutarlo en segundo plano introduciremos:

`$ python server.py &`

**Ejecución del cliente**

En el directorio donde ejecutemos el cliente deberá existir una carpeta denominada **Recibido**. Ejecutaremos el programa introduciendo:

`$ python client.py`

Una vez lanzado el programa, nos solicitará la dirección ip del servidor y el puerto en el que éste está corriendo. Si pulsamos intro sin introducir nada, tomará el valor por defecto (localhost:5059).

Para obtener una lista y descripción de los comandos admitidos se deberá de proceder a la lectura de la **sección 4.2 de la documentación** (o introducir un comando erróneo).
