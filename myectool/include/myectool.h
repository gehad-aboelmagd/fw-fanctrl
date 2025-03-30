#ifndef MYLIB_H
#define MYLIB_H

#include <stdint.h>

/* Max temp sensor entries for host commands */
#define MAX_TEMP_SENSOR_ENTRIES 24

const char *sensors_names[] = {
    "CPU", "Battery", "Board"
};

struct result_array {
    int size;
    int *arr;
};

struct sensor_info {
    uint8_t sensor_id;
	uint8_t sensor_type;
    char sensor_name[32];
};

struct result_struct {
    int size;
    struct sensor_info *sensors;
};

#ifdef __cplusplus
extern "C" {
#endif

bool is_battery_on_ac();
bool run_auto_fan_ctrl();
bool set_fanduty(long speed);
int get_sensor_temp(long sensor_id);
struct result_struct get_sensors_info();
struct result_array get_all_sensor_temps();

#ifdef __cplusplus
}
#endif

#endif