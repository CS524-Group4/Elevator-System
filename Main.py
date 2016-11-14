from Elevator_System import ElevatorSystem
from Sensors.Weight_Sensor import WeightSensor
from GUI.Inside_GUI import Inside_GUI

q1 = ElevatorSystem()
ws = WeightSensor()
i_gui = Inside_GUI()
i_gui.set_system(q1)
