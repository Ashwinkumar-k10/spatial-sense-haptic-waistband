/**
 * SPATIAL-SENSE Firmware - Sensor Scheduler Implementation
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#include "sensor_scheduler.h"

SensorScheduler::SensorScheduler() : _wire(nullptr), _currentStep(0), _lastFireTime(0) {
    for (int i = 0; i < NUM_SENSORS; i++) {
        _measurements[i].channel = i;
        _measurements[i].elevation_deg = (i % 2 == 0) ? 0 : 25;
        _measurements[i].azimuth_deg = i * 45;
        _measurements[i].distance_mm = 4000;
        _measurements[i].status = 0;
        _measurements[i].timestamp_ms = 0;
        for (int j = 0; j < 3; j++) _history[i][j] = 4000;
    }
}

bool SensorScheduler::begin(TwoWire &wirePort, int sdaPin, int sclPin) {
    _wire = &wirePort;
    _wire->begin(sdaPin, sclPin, 400000); // 400 kHz Fast-Mode I2C
    
    // Test TCA9548A connection
    _wire->beginTransmission(TCA9548A_ADDR);
    if (_wire->endTransmission() != 0) {
        return false;
    }
    return true;
}

void SensorScheduler::selectMuxChannel(uint8_t channel) {
    if (channel > 7) return;
    _wire->beginTransmission(TCA9548A_ADDR);
    _wire->write(1 << channel);
    _wire->endTransmission();
}

uint16_t SensorScheduler::applyMedianFilter(uint8_t channel, uint16_t rawDist) {
    _history[channel][2] = _history[channel][1];
    _history[channel][1] = _history[channel][0];
    _history[channel][0] = rawDist;
    
    uint16_t a = _history[channel][0];
    uint16_t b = _history[channel][1];
    uint16_t c = _history[channel][2];
    
    if ((a <= b && b <= c) || (c <= b && b <= a)) return b;
    if ((b <= a && a <= c) || (c <= a && a <= b)) return a;
    return c;
}

void SensorScheduler::updateInterleavedFiring() {
    uint32_t now = millis();
    if (now - _lastFireTime >= PHASE_OFFSET_MS) {
        _lastFireTime = now;
        uint8_t ch = _firingSequence[_currentStep];
        selectMuxChannel(ch);
        
        // Non-blocking read simulation / hardware transaction
        uint16_t rawDist = 1200; // In production: read from VL53L1X register
        _measurements[ch].distance_mm = applyMedianFilter(ch, rawDist);
        _measurements[ch].timestamp_ms = now;
        
        _currentStep = (_currentStep + 1) % NUM_SENSORS;
    }
}

SensorMeasurement SensorScheduler::getMeasurement(uint8_t channel) {
    if (channel < NUM_SENSORS) return _measurements[channel];
    return _measurements[0];
}

void SensorScheduler::getAllMeasurements(SensorMeasurement outBuffer[NUM_SENSORS]) {
    for (int i = 0; i < NUM_SENSORS; i++) {
        outBuffer[i] = _measurements[i];
    }
}
