#!/usr/bin/env python
# -*- coding: utf-8 -*-
# GRUPO 1
# Emilio Bello
# Juan Carlos de la Torre
# Manuel Francisco
# Jose Manuel Vidal

import sys
import zmq
import sha
import time

direccion = raw_input('Bienvenido. Introduce dirección y puerto del servidor. (Por defecto localhost:5059)\n< ')
username = raw_input('Introduce nombre de usuario\n< ')
password = raw_input('Introduce contraseña\n< ')

if direccion == '':
	direccion = 'localhost:5059'

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.plain_username = username
socket.plain_password = password
socket.connect('tcp://' + direccion)

while True:
	try:
		#Prompt
		comando = raw_input('> ')
		
		#Procesar el comando introducido
		if comando == 'ls':
			#Listar ficheros en el servidor
			socket.send('LS')
			print socket.recv(),
		
		
		elif 'get ' in comando:
			#Obtener un fichero del servidor.
			#Enviamos la petición al servidor: GET nombrefichero
			peticion = comando.replace('get ', 'GET ', 1)
			socket.send(peticion)
			respuesta = socket.recv()
			
			if respuesta == 'OK':
				#Abrimos el fichero donde vamos a guardar lo que nos envie el
				#servidor
				guardar = open('Recibido/' + comando.replace('get ', '', 1), 'wb')
				
				#Avisamos de que estamos preparados
				socket.send('READY')
				
				#Escribimos la respuesta
				guardar.write(socket.recv())
				guardar.close()
				
			elif respuesta == 'NOT FOUND':
				#El fichero no existe. Alertar y no hacer nada
				print 'El fichero no existe en el servidor. Abortado.'
				
			else:
				print 'Algo no ha ido bien...'
			
		
		elif 'put ' in comando:
			#Subir un fichero al servidor.
			#Enviamos la petición al servidor: PUT nombrefichero
			peticion = comando.replace('put ', 'PUT ', 1)
			socket.send(peticion)
			#Abrimos el fichero a enviar
			fichero = comando.replace('put ', '', 1)
			flujo = open('Recibido/' + fichero, 'rb')
			
			#Leemos el estado del servidor
			respuesta = socket.recv()
			if respuesta == 'READY':
				#El servidor está listo. Enviamos el fichero.
				socket.send(flujo.read())
				
				#Leemos la respuesta
				respuesta = socket.recv()
				
				if respuesta == 'DONE':
					#Todo correcto.
					print 'Fichero enviado.'
				elif respuesta == 'ERROR':
					#Algo ha ido mal
					print 'Algo ha ido mal... fichero no enviado.'
			
			elif 'READY' not in respuesta:
				#Si el servidor no está listo, es porque ya existe un
				#fichero con el mismo nombre. Nos enviará por tanto el hash.
				#Comprobamos si es el mismo.
				s = sha.new()
				s.update(fichero)
				leido = flujo.read(1024)
				while len(leido) != 0:
					s.update(leido)
					leido = flujo.read(1024)
				
				if s.hexdigest() == respuesta:
					#El fichero es el mismo. No se hace nada.
					print 'El fichero ya está en el servidor.'
				else:
					#El fichero no es el mismo. Preguntar si queremos
					#sobreescribir
					print 'El fichero ', fichero, ', ya existe en el servidor, con un contenido distinto. ¿Continuar?'
					p = raw_input('(Y/N) ')
					
					if 'Y' == p or 'y' == p:
						#Sobreescribir.
						socket.send('OVERWRITE')
						respuesta = socket.recv()
						
						if respuesta == 'READY':
							flujo.seek(0, 0)
							socket.send(flujo.read())
							
							respuesta = socket.recv()
				
							if respuesta == 'DONE':
								print 'Fichero enviado.'
							elif respuesta == 'ERROR':
								print 'Algo ha ido mal... fichero no enviado.'
					
					elif 'N' == p or 'n' == p:
						#No hacer nada. Comunicar al servidor que todo
						#correcto y paramos.
						socket.send('OK')
						socket.recv()
					else:
						#El usuario ha introducido algo distinto a Y/y/N/n
						#No hacer nada. Comunicar al servidor que todo
						#correcto y paramos.
						print 'Respuesta incorrecta. Abortado.'
						socket.send('OK')
						socket.recv()
		elif 'rm ' in comando:
			#Borrar un fichero del servidor.
			socket.send(comando.replace('rm ', 'RM ', 1))
			respuesta = socket.recv()
			
			if respuesta == 'NOT FOUND':
				#El fichero no existe
				print 'El fichero no existe en el servidor'
			elif 'DONE' not in respuesta:
				#La respuesta no ha sido ni NOT FOUND ni DONE.
				#Algo ha ido mal.
				print 'Algo ha ido mal...'
				
			
		elif comando == 'quit':
			print '¡Adiós!'
			break
			
		elif comando == 'ping':
			tic = time.time()
			socket.send('PING!')
			respuesta = socket.recv()
			toc = time.time()
			
			print respuesta, ' ', (toc-tic), ' s.'
		else:
			print 'Comando no encontrado.'
			print 'ls          \tLista los ficheros en el servidor remoto.'
			print 'get <nombre>\tDescarga el fichero <nombre> del servidor remoto.'
			print 'put <nombre>\tSube el fichero <nombre> al servidor remoto.'
			print 'rm  <nombre>\tElimina el fichero <nombre> del servidor remoto.'
			print 'ping        \tRealiza ping al servidor.'
	except KeyboardInterrupt:
		print('\n¡Adiós!')
		sys.exit()
