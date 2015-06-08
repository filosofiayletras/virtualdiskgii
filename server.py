#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GRUPO 1
# Emilio Bello
# Juan Carlos de la Torre
# Manuel Francisco
# Jose Manuel Vidal

import zmq
import zmq.auth
from zmq.auth.thread import ThreadAuthenticator
import os
import sha
import sys

context = zmq.Context()

auth = ThreadAuthenticator(context)
auth.start()
auth.configure_plain(domain='*', passwords=
{
	'admin': 'admin',
	'user': 'user'
})

socket = context.socket(zmq.REP)
socket.plain_server = True
socket.bind("tcp://*:5059")

while True:
	try:
		#Leer comando del cliente
		comando = socket.recv()
		
		if comando == 'LS':
			#Listar.
			resultado = ''
			listado = os.listdir('Compartir/')

			#Para cada fichero en Compartir/, calcular su hash y enviar
			#nombre y hash
			for fichero in listado:
				s = sha.new()
				s.update(fichero)
				flujo = open('Compartir/' + fichero, 'rb')
				
				leido = flujo.read(1024)
				while len(leido) != 0:
					s.update(leido)
					leido = flujo.read(1024)
				
				resultado += fichero + '\t' + s.hexdigest() + '\n'
		
			#Enviar listado
			socket.send(resultado)
			
			
		elif 'GET' in comando:
			#El cliente quiere que enviemos un fichero
			nombre = comando.replace('GET ', '', 1)
			
			if os.path.isfile('Compartir/' + nombre):
				#El fichero existe.
				socket.send('OK')
				respuesta = socket.recv()
				
				if respuesta == 'READY':
					#Abrimos el fichero y lo enviamos
					flujo = open('Compartir/' + nombre, 'rb')
					socket.send(flujo.read())
					flujo.close()
			else:
				socket.send('NOT FOUND')
			
			
		elif 'PUT' in comando:
			#El cliente quiere enviarnos un fichero
			nombre = comando.replace('PUT ', '', 1)
			
			if os.path.isfile('Compartir/' + nombre):
				#El fichero existe. Lo abrimos y enviamos el hash para ver
				#si es el mismo.
				flujo = open('Compartir/' + nombre, 'rb')
				s = sha.new()
				s.update(nombre)
				
				leido = flujo.read(1024)
				while len(leido) != 0:
					s.update(leido)
					leido = flujo.read(1024)
				
				flujo.close()
				
				
				#Enviamos el hash calculado.
				socket.send(s.hexdigest())
				
				#Esperamos a la respuesta del cliente
				respuesta = socket.recv()
				
				if respuesta == 'OK':
					#El fichero es el mismo. No hacer nada.
					socket.send('')
				elif respuesta == 'OVERWRITE':
					#El cliente quiere sobreescribir.
					flujo = open('Compartir/' + nombre, 'wb')
					socket.send('READY')
					flujo.write(socket.recv())
					flujo.close()
					socket.send('DONE')
			
			else:
				#El fichero no existe. Abrimos el flujo y escribimos.
				flujo = open('Compartir/' + nombre, 'wb')
				socket.send('READY')
				flujo.write(socket.recv())
				flujo.close()
				socket.send('DONE')
			
		
		elif 'RM ' in comando:
			#El cliente quiere borrar un fichero
			nombre = comando.replace('RM ', '', 1)
			
			if os.path.isfile('Compartir/' + nombre):
				#El fichero existe. Lo borramos.
				os.remove('Compartir/' + nombre)
				socket.send('DONE')
			else:
				#El fichero no existe.
				socket.send('NOT FOUND')
		
		elif comando == 'PING!':
			socket.send('PONG!')
	except KeyboardInterrupt:
		auth.stop()
		print '\n¡Adiós!'
		sys.exit()
