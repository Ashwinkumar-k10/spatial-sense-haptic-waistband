/**
 * SPATIAL-SENSE Firmware - Haptic Engine (Core 1)
 * Distance-to-Cadence Mapping & Resonant Actuation (205 Hz LRA)
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#ifndef HAPTIC_ENGINE_H
#define HAPTIC_ENGINE_H

#include <Arduino.h>
#include <Wire.h>

#define NUM_ACTUATORS 8
#define LRA_RESONANCE_FREQ_HZ 205
#define MAX_CADENCE_HZ 12
#define MIN_CADENCE_INTERVAL_MS 1200
#define ALERT_DECAY_WINDOW_MS 3000

class HapticEngine {
public:
    HapticEngine();
    bool begin(TwoWire &wirePort = Wire1, int sdaPin = 15, int sclPin = 16);
    void updateCadence(uint8_t node, uint16_t distance_mm, bool userMoving);
    void triggerZeroSightSelfTest();
    void stopAll();

private:
    TwoWire* _wire;
    uint32_t _lastPulseTime[NUM_ACTUATORS];
    uint32_t _stationaryStartTime[NUM_ACTUATORS];
    uint16_t _lastDistance[NUM_ACTUATORS];
    
    uint16_t mapDistanceToInterval(uint16_t dist_mm);
    void pulseActuator(uint8_t node, uint8_t intensity);
};

#endif // HAPTIC_ENGINE_H
