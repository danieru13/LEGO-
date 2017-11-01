from BrickPi import *

import sys, tty, termios, time

#Mover
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
	termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

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
BrickPi.MotorEnable[motorDer] = 1
BrickPi.MotorEnable[motorIzq] = 1

while True:
	char = getch()
	if(char != "w" and char != "a" and char != "s" and char != "d" and != "x"):
		print("Esperando comando")
		char = getch()
	else:
		if (char == "w"):
			acelerar()
		if (char == "s"):
			retroceder()
		if (char == "a"):
			izquierda()
		if (char == "d"):
			derecha()		
		if (char == "x"):
			break
BrickPiUpdateValues()
char = getch()
time.sleep(.1)				
