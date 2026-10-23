/**
 * SPATIAL-SENSE Firmware - Low-Power & Motion Manager (ULP / Core 0)
 * Bosch BMI160 6-DOF IMU Motion Sensing & 15 uA Light Sleep
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#ifndef POWER_MANAGER_H
#define POWER_MANAGER_H

#include <Arduino.h>

class PowerManager {
public:
    PowerManager();
    bool begin(int imuIntPin = 3);
    bool isUserMoving();
    void checkPowerState();
    uint16_t getBatteryMilliVolts();
    uint8_t getBatteryPercent();

private:
    int _intPin;
    bool _moving;
    uint32_t _lastMotionTime;
};

#endif // POWER_MANAGER_H
