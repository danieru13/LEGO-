from BrickPi import *
import threading

BrickPiSetup()
motorIzq = PORT_C #Puerto motor izquierda
motorDer = PORT_B #Puerto motor derecho
motor3 = PORT_D #Puerto motor trasero
sensorIzquierdo = PORT_1
sensorDerecho = PORT_2
BrickPi.MotorEnable[motorDer] = 1
BrickPi.MotorEnable[motorIzq] = 1
BrickPi.MotorEnable[motor3] = 1
colors=["Black","Blue","Green","Yellow","Red", "White","Brown"]


def acelerar():
        #Mover hacia adelante.
        BrickPi.MotorSpeed[motorDer] = 50
        BrickPi.MotorSpeed[motorIzq] = 50
        BrickPi.MotorSpeed[motor3] = -50
        print("acelerar")
def derecha():
        #Mover hacia la derecha.
        BrickPi.MotorSpeed[motorDer] = -25
        BrickPi.MotorSpeed[motorIzq] = 25
        BrickPi.MotorSpeed[motor3] = 0
        print("derecha")
def izquierda():
        #Mover hacia la izquierda.
        BrickPi.MotorSpeed[motorDer] = 25
        BrickPi.MotorSpeed[motorIzq] = -25
        BrickPi.MotorSpeed[motor3] = 0
        print("izquierda")


class hiloIzquierdo(threading.Thread):
    def __init__(self,threadID, name, counter):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
    def run(self):
        BrickPi.SensorType[sensorIzquierdo] = TYPE_SENSOR_EV3_COLOR_M2
        BrickPiSetupSensors()
        BrickPi.SensorType[sensorDerecho] = TYPE_SENSOR_EV3_COLOR_M2
        BrickPiSetupSensors()

thread1 = hiloIzquierdo(1, "Thread-1", 1) #Inicia el hilo
thread1.setDaemon(True)
thread1.start()
time.sleep(3)

while True:

    resultado = BrickPiUpdateValues()

    if not resultado:
    	
        izquierdo = BrickPi.Sensor[sensorIzquierdo]
        derecho = BrickPi.Sensor[sensorDerecho]
        print(str(izquierdo)+ "<------Izquierdo Derecho------>"+str(derecho))
        if(derecho != 1 and izquierdo!=1):
            acelerar()
            BrickPiUpdateValues()
            time.sleep(0.021)
        elif (derecho == 1 and izquierdo == 6):
            derecha()
            BrickPiUpdateValues()
            time.sleep(0.021)
        elif (derecho == 6 and izquierdo == 1):
            izquierda()
            BrickPiUpdateValues()
            time.sleep(0.021)