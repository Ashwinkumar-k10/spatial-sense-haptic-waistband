/**
 * SPATIAL-SENSE Firmware - Power Manager Implementation
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#include "power_manager.h"

PowerManager::PowerManager() : _intPin(3), _moving(true), _lastMotionTime(0) {}

bool PowerManager::begin(int imuIntPin) {
    _intPin = imuIntPin;
    pinMode(_intPin, INPUT_PULLUP);
    _lastMotionTime = millis();
    return true;
}

bool PowerManager::isUserMoving() {
    if (digitalRead(_intPin) == LOW) {
        _lastMotionTime = millis();
        _moving = true;
    } else if (millis() - _lastMotionTime > 5000) {
        _moving = false;
    }
    return _moving;
}

void PowerManager::checkPowerState() {
    if (!_moving && (millis() - _lastMotionTime > 15000)) {
        // Enter 15 uA light sleep; ULP maintains IMU step wake interrupt
        // esp_light_sleep_start();
    }
}

uint16_t PowerManager::getBatteryMilliVolts() {
    int raw = analogRead(4); // ADC voltage divider
    return (uint16_t)((raw / 4095.0) * 3.3 * 2.0 * 1000);
}

uint8_t PowerManager::getBatteryPercent() {
    uint16_t mv = getBatteryMilliVolts();
    if (mv >= 4200) return 100;
    if (mv <= 3300) return 0;
    return (uint8_t)((mv - 3300) * 100 / (4200 - 3300));
}
