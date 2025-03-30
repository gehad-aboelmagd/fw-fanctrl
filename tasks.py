import os
from invoke import task

lib_name = "myectool"
lib_path = os.path.join(os.path.dirname(__file__), "src", "fw_fanctrl", "hardwareController", "lib")

@task
def build(c):
    print("=======================================")
    print("Building into .so")
    try:
        c.run(f"g++ -shared -fPIC -I {lib_name}/include -o {lib_path}/{lib_name}.so {lib_name}/src/{lib_name}.cc")
    except:
        print("an error occurred!")
    else:
        print("*completed")

@task
def testlib(c):
    print("=======================================")
    print(f"testing {lib_name}")

    import ctypes
    mylib = ctypes.CDLL(f"{lib_path}/{lib_name}.so")

    class SensorInfo(ctypes.Structure):
        _fields_ = [
            ("sensor_id", ctypes.c_uint8),
            ("sensor_type", ctypes.c_uint8),
            ("sensor_name", ctypes.c_char*32)
        ]

    class ResultStruct(ctypes.Structure):
        _fields_ = [
            ("size", ctypes.c_int),
            ("sensor_info", ctypes.POINTER(SensorInfo))
        ]

    mylib.get_sensors_info.restype = ResultStruct
    result = mylib.get_sensors_info()
    print("Getting Sensors Info...")
    print("<sensor-id> <sensor_type> <sensor-name>")
    for i in range(result.size):
        print(result.sensor_info[i].sensor_id,
              result.sensor_info[i].sensor_type,
              result.sensor_info[i].sensor_name)


    class ResultArray(ctypes.Structure):
        _fields_ = [
            ("size", ctypes.c_int),
            ("sensors_temp", ctypes.POINTER(ctypes.c_int))
        ]
    
    mylib.get_all_sensor_temps.restype = ResultArray
    result = mylib.get_all_sensor_temps()
    print("Getting Sensors Temperatures...")
    for i in range(result.size):
        print(i, result.sensors_temp[i])

    mylib.get_sensor_temp.argtypes = [ctypes.c_long]
    mylib.get_sensor_temp.restype = ctypes.c_int
    sensor_id = 3
    sensor_temp = mylib.get_sensor_temp(sensor_id)
    print("Getting a Specific Sensor Temperature...")
    print("<sensor-id> <sensor-temp>")
    print(sensor_id, sensor_temp)

    mylib.set_fanduty.argtypes = [ctypes.c_long]
    mylib.set_fanduty.restype = ctypes.c_bool
    speed = 20
    is_set = mylib.set_fanduty(speed)
    print("Setting fanduty given specific speed...")
    print("<required-speed> <is-set>")
    print(speed, is_set)

    mylib.is_battery_on_ac.restype = ctypes.c_bool
    is_set = mylib.is_battery_on_ac()
    print("Querying If Battery Is On AC...")
    print(is_set)

    mylib.run_auto_fan_ctrl.restype = ctypes.c_bool
    is_set = mylib.run_auto_fan_ctrl()
    print("Running Auto Fan Control...")
    print(is_set)

@task(pre=[build, testlib])
def all(c):
    ...