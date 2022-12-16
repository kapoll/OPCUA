#BIBLIOTEKI
from opcua import Client
import time
import numpy as np
from random import choice

#PODŁĄCZENIE DO SERWERA
url = "opc.tcp://127.0.0.1:1888"               #PODAĆ ODPOWIEDNIE IP SERWERA

client= Client(url)                                 
client.connect()                                    #ŁĄCZENIE Z SERWEREM
print("Client Connected")

while True:
    #GETTING NODES
    ekstruder_array = client.get_node("ns=2;i=10")
    piston_value = client.get_node("ns=2;i=12")
    pump_pressure = client.get_node("ns=2;i=14")
    actuator_position = client.get_node("ns=2;i=16")

    #GENERATE EXTRUDER DATA
    extruder_speed = np.random.uniform(1.0,10.0)
    extruder_temp1 = np.random.uniform(1.0,190.0)
    extruder_temp2 = np.random.uniform(1.0,280.0)

    #GENERATE DATA TO SEND
    extruder_data = [extruder_speed, extruder_temp1, extruder_temp2]
    piston_released = choice([True, False])
    actual_pump_pressure = np.random.randint(20,1000)
    actuator_pos = np.random.randint(0,20000)

    #SENDING DATA TO SERVER
    ekstruder_array.set_value(extruder_data)
    piston_value.set_value(piston_released)
    pump_pressure.set_value(actual_pump_pressure)
    actuator_position.set_value(actuator_pos)

    time.sleep(5)