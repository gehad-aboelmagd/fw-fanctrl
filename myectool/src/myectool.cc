#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "myectool.h"

bool is_battery_on_ac() {
    bool is_on_ac = true;
    return is_on_ac;
}

bool run_auto_fan_ctrl() {
    bool is_auto_controlled = true;
    return is_auto_controlled;
}

bool set_fanduty(long speed) {
    bool is_correctly_set = true;
    return is_correctly_set;
}

int get_sensor_temp(long sensor_id){
    
    static int sensor_temp = 45 + rand() % 5;
    return sensor_temp;
}

struct result_array get_all_sensor_temps() {
    static int sensors_temp[MAX_TEMP_SENSOR_ENTRIES];
    for(int i=0; i<MAX_TEMP_SENSOR_ENTRIES; i++) {
        sensors_temp[i] = 45 + rand() % 5;
    }

    static struct result_array result;
    result.size = MAX_TEMP_SENSOR_ENTRIES;
    result.arr = sensors_temp;

    return result;
}

struct result_struct get_sensors_info() {
    static struct sensor_info sensors[MAX_TEMP_SENSOR_ENTRIES];
    for(int i=0; i<MAX_TEMP_SENSOR_ENTRIES; i++) {
        sensors[i].sensor_id = i;
        sensors[i].sensor_type = 1 + rand() % 5;
        strcpy(sensors[i].sensor_name, sensors_names[rand()%3]);
    }

    static struct result_struct result;
    result.size = MAX_TEMP_SENSOR_ENTRIES;
    result.sensors = sensors;
    return result;
}
