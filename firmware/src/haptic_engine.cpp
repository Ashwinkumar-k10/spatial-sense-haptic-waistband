/**
 * SPATIAL-SENSE Firmware - Haptic Engine Implementation
 * Team Techtonics - Vishwakarma Awards 2026-27
 */

#include "haptic_engine.h"

HapticEngine::HapticEngine() : _wire(nullptr) {
    for (int i = 0; i < NUM_ACTUATORS; i++) {
        _lastPulseTime[i] = 0;
        _stationaryStartTime[i] = 0;
        _lastDistance[i] = 4000;
    }
}

bool HapticEngine::begin(TwoWire &wirePort, int sdaPin, int sclPin) {
    _wire = &wirePort;
    _wire->begin(sdaPin, sclPin, 400000);
    return true;
}

uint16_t HapticEngine::mapDistanceToInterval(uint16_t dist_mm) {
    if (dist_mm >= 2500) return 0; // Out of warning threshold
    if (dist_mm <= 400) return 1000 / MAX_CADENCE_HZ; // 83 ms = 12 Hz emergency burst
    
    // Linear interpolation between 2500mm (1200ms) and 400mm (83ms)
    float ratio = (float)(dist_mm - 400) / (2500 - 400);
    return (uint16_t)(83 + ratio * (MIN_CADENCE_INTERVAL_MS - 83));
}

void HapticEngine::pulseActuator(uint8_t node, uint8_t intensity) {
    // In production: send register command to DRV2605L on dedicated bus
    // Auto-resonance tracking maintains 205 Hz ± 3 Hz mechanically
}

void HapticEngine::updateCadence(uint8_t node, uint16_t distance_mm, bool userMoving) {
    if (node >= NUM_ACTUATORS) return;
    
    uint32_t now = millis();
    uint16_t interval = mapDistanceToInterval(distance_mm);
    
    if (interval == 0) return;
    
    // Anti-fatigue alert decay window: 3-second intensity ramp-down if user pauses
    uint8_t intensity = 255;
    if (!userMoving) {
        if (_stationaryStartTime[node] == 0) {
            _stationaryStartTime[node] = now;
        } else if (now - _stationaryStartTime[node] >= ALERT_DECAY_WINDOW_MS) {
            intensity = 90; // Decay to 35% to prevent receptor adaptation
        }
    } else {
        _stationaryStartTime[node] = 0;
    }
    
    if (now - _lastPulseTime[node] >= interval) {
        _lastPulseTime[node] = now;
        pulseActuator(node, intensity);
    }
}

void HapticEngine::triggerZeroSightSelfTest() {
    // Clockwise verification sweep across all 8 nodes
    for (int i = 0; i < NUM_ACTUATORS; i++) {
        pulseActuator(i, 200);
        delay(120);
    }
}

void HapticEngine::stopAll() {
    for (int i = 0; i < NUM_ACTUATORS; i++) {
        pulseActuator(i, 0);
    }
}
