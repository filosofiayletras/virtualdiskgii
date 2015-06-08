# README #

# VirtualDiskGII #

## Justificaci�n ##

Una de las peticiones m�s concurrentes entre alumnos de tercero y cuarto curso del grado de ingenier�a inform�tica es la de documentaci�n de una especialidad diferente a la que est�s cursando. Queramos o no, son muchas las ocasiones en las que las menciones se entrelazan, siendo necesario tener conocimientos de unas para elaborar trabajos de calidad en otras.

En primer y segundo curso es habitual el uso de una carpeta en dropbox para compartir todo tipo de informaci�n, convirti�ndose en un servidor de experiencias de a�os anteriores donde algunos aportan y todos consumen. En primero, el que aporta lo hace de buena f�, sin poner en cuesti�n el feedback de sus aportaciones. En segundo, la situaci�n es similar, pero ya los aportadores empiezan a balancear lo aportado frente a lo recibido, balance que suele salir negativo y que provoca el abandono de dicha actividad aportadora.

En tercero y cuarto, el celo por lo propio es el gran dominante. Es muy complicado encontrar a alguien dispuesto a compartir. O por lo menos gratuitamente. Si deseas informaci�n, debes pagar con informaci�n. 

Y es en esta situaci�n donde hemos puesto nuestro punto de mira. La pregunta es: �Qu� podemos ofrecer a los alumnos de tercero y cuarto que facilite el intercambio de informaci�n?

La respuesta es clara. Deber�amos ofrecer a los alumnos un sistema cliente-servidor. Dicho sistema debe permitir a un usuario ofrecer sus ficheros a los dem�s a trav�s de la red de la UCA. Pero, para poder salvaguardar el celo existente, el que ofrece los ficheros debe poder controlar qui�nes acceden al mismo.

## Objetivo. ##

Proveer de una solucion para que las personas autorizadas a acceder a un servidor puedan intercambiar ficheros.

## Ubicaci�n de los ficheros. ##

* C�digo fuente: Carpeta ra�z.
* Documentaci�n: Carpeta ./docs

## Instalacion y Funcionamiento ##

**Ejecuci�n del servidor**

En el directorio donde ejecutemos el servidor deber� contener una carpeta denominada **Compartir**. Si deseamos autorizar a un usuario, deberemos hacerlo en la estructura para tal fin existente en el c�digo. En Linux, para ejecutarlo en segundo plano introduciremos:

`$ python server.py &`

**Ejecuci�n del cliente**

En el directorio donde ejecutemos el cliente deber� existir una carpeta denominada **Recibido**. Ejecutaremos el programa introduciendo:

`$ python client.py`

Una vez lanzado el programa, nos solicitar� la direcci�n ip del servidor y el puerto en el que �ste est� corriendo. Si pulsamos intro sin introducir nada, tomar� el valor por defecto (localhost:5059).

Para obtener una lista y descripci�n de los comandos admitidos se deber� de proceder a la lectura de la **secci�n 4.2 de la documentaci�n** (o introducir un comando err�neo).
