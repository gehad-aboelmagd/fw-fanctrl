import os
from abc import ABC
from ctypes import CDLL
from ctypes import Structure, POINTER, c_bool, c_char, c_uint8, c_int, c_long

from fw_fanctrl.hardwareController.HardwareController import HardwareController

class ResultArray(Structure):
    _fields_ = [
        ("size", c_int),
        ("sensors_temp", POINTER(c_int))
    ]
    
class SensorInfo(Structure):
    _fields_ = [
        ("sensor_id", c_uint8),
        ("sensor_type", c_uint8),
        ("sensor_name", c_char*32)
    ]

class ResultStruct(Structure):
    _fields_ = [
        ("size", c_int),
        ("sensor_info", POINTER(SensorInfo))
    ]

class EctoolHardwareController(HardwareController, ABC):
    myectool = None
    noBatterySensorMode = False
    nonBatterySensors = None

    def __init__(self, no_battery_sensor_mode=False):
        lib_path = os.path.join(os.path.dirname(__file__), "lib")
        self.myectool = CDLL(f"{lib_path}/myectool.so")
        if no_battery_sensor_mode:
            self.noBatterySensorMode = True
            self.populate_non_battery_sensors()

    def populate_non_battery_sensors(self):
        self.nonBatterySensors = []
        self.myectool.get_sensors_info.restype = ResultStruct
        result = self.myectool.get_sensors_info()
        battery_sensors = []
        for i in range(result.size):
            if result.sensor_info[i].sensor_name == "Battery":
                battery_sensors.append(result.sensor_info[i].sensor_type)
        for i in range(result.size):
            if result.sensor_info[i].sensor_id not in battery_sensors:
                self.nonBatterySensors.append(result.sensor_info[i].sensor_id)

    def get_temperature(self):
        temps = []
        if self.noBatterySensorMode:
            self.myectool.get_sensor_temp.argtypes = [c_long]
            self.myectool.get_sensor_temp.restype = c_int
            for x in self.nonBatterySensors:
                temps.append(self.myectool.get_sensor_temp(x)) 
        else:
            self.myectool.get_all_sensor_temps.restype = ResultArray
            result = self.myectool.get_all_sensor_temps()
            for i in range(result.size):
                temps.append(result.sensors_temp[i])
        temps = sorted([x for x in temps if x > 0], reverse=True)
        # safety fallback to avoid damaging hardware
        if len(temps) == 0:
            return 50
        return float(round(temps[0], 2))

    def set_speed(self, speed):
        self.myectool.set_fanduty.argtypes = [c_long]
        self.myectool.set_fanduty.restype = c_bool
        self.myectool.set_fanduty(speed)

    def is_on_ac(self):
        self.myectool.is_battery_on_ac.restype = c_bool
        return self.myectool.is_battery_on_ac()

    def pause(self):
        self.myectool.run_auto_fan_ctrl.restype = c_bool
        self.myectool.run_auto_fan_ctrl()

    def resume(self):
        # Empty for ectool, as setting an arbitrary speed disables the automatic fan control
        pass
