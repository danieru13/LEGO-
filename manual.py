from BrickPi import *

import sys, tty, termios, time #Se importan librearias

#Funcion para recibir caracteres del teclado
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch
#Funciones de movimiento que indican a los motores a que velocidad revolucionar
def acelerar():
	#Mover hacia adelante.
	BrickPi.MotorSpeed[motorDer] = 255
	BrickPi.MotorSpeed[motorIzq] = 255
def retroceder():
	#Mover hacia atras.
	BrickPi.MotorSpeed[motorDer] = -50
	BrickPi.MotorSpeed[motorIzq] = -50
def derecha():
	#Mover hacia la derecha.
	BrickPi.MotorSpeed[motorDer] = -255
	BrickPi.MotorSpeed[motorIzq] = 255
def izquierda():
	#Mover hacia la izquierda.
	BrickPi.MotorSpeed[motorDer] = 255
	BrickPi.MotorSpeed[motorIzq] = -255

BrickPiSetup() 
motorIzq = PORT_C #Puerto motor izquierda
motorDer = PORT_B #Puerto motor derecho
BrickPi.MotorEnable[motorDer] = 1 #Habilita motor derecho
BrickPi.MotorEnable[motorIzq] = 1 #Habilita motor izquierdo

#Ciclo para recibir comandos
while True:
	char = getch() #Recibe comando de teclado
	if(char != "w" and char != "a" and char != "s" and char != "d" and != "x"):
		print("Esperando comando")
		char = getch()
	else:
		#Si recibe w acelera
		if (char == "w"):
			acelerar()
		#Si recibe s retrocede
		if (char == "s"):
			retroceder()
		#Si recibe a gira a la izquierda
		if (char == "a"):
			izquierda()
		#Si recibe d gira a la derecha	
		if (char == "d"):
			derecha()
		#Si recibe x se rompe el ciclo y termina el codigo	
		if (char == "x"):
			break
BrickPiUpdateValues() #Actualiza valores
char = getch() #Recibe caracteres
time.sleep(.1) #Le da una pausa al codigo para que los motores puedan actualizarse			
