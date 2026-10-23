/**
 * SPATIAL-SENSE Firmware - Sensor Scheduler (Core 0)
 * Dual-Elevation ToF LiDAR Scheduler with Interleaved Crosstalk Mitigation
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#ifndef SENSOR_SCHEDULER_H
#define SENSOR_SCHEDULER_H

#include <Arduino.h>
#include <Wire.h>

#define TCA9548A_ADDR 0x70
#define NUM_SENSORS 8
#define SENSOR_REFRESH_RATE_HZ 15
#define PHASE_OFFSET_MS 4

struct SensorMeasurement {
    uint8_t channel;
    uint8_t elevation_deg; // 0 or 25
    int16_t azimuth_deg;   // 0, 45, 90, 135, 180, 225, 270, 315
    uint16_t distance_mm;
    uint8_t status;        // 0 = Valid, 1 = Out of Range, 2 = Dropout
    uint32_t timestamp_ms;
};

class SensorScheduler {
public:
    SensorScheduler();
    bool begin(TwoWire &wirePort = Wire, int sdaPin = 1, int sclPin = 2);
    void updateInterleavedFiring();
    SensorMeasurement getMeasurement(uint8_t channel);
    void getAllMeasurements(SensorMeasurement outBuffer[NUM_SENSORS]);

private:
    TwoWire* _wire;
    SensorMeasurement _measurements[NUM_SENSORS];
    const uint8_t _firingSequence[NUM_SENSORS] = {0, 4, 1, 5, 2, 6, 3, 7}; // 1->5->2->6->3->7->4->8 (0-indexed)
    uint8_t _currentStep;
    uint32_t _lastFireTime;
    
    void selectMuxChannel(uint8_t channel);
    uint16_t applyMedianFilter(uint8_t channel, uint16_t rawDist);
    uint16_t _history[NUM_SENSORS][3];
};

#endif // SENSOR_SCHEDULER_H
