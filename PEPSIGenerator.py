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
    extruder_speed = round(np.random.uniform(1.0,10.0), 2)
    extruder_temp1 = round(np.random.uniform(1.0,180.0), 2)
    extruder_temp2 = round(np.random.uniform(1.0,160.0), 2)

    #GENERATE TIMELINE DATA
    acutator_pos1 = np.random.randint(0,5)
    acutator_pos2 = np.random.randint(0,5)
    acutator_pos3 = np.random.randint(0,5)

    #GENERATE DATA TO SEND
    extruder_data = [extruder_speed, extruder_temp1, extruder_temp2]
    piston_released = choice([True, False])
    actual_pump_pressure = np.random.randint(20,100)
    actuator_pos = [acutator_pos1, acutator_pos2, acutator_pos3]

    #PRINTING IN CONSOLE
    print("-------------")
    print(extruder_data)
    print(piston_released)
    print(actual_pump_pressure)
    print(actuator_pos)
    print("-------------")

    #SENDING DATA TO SERVER
    ekstruder_array.set_value(extruder_data)
    piston_value.set_value(piston_released)
    pump_pressure.set_value(actual_pump_pressure)
    actuator_position.set_value(actuator_pos)

    time.sleep(5)