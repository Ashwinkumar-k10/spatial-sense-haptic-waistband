/**
 * SPATIAL-SENSE Firmware - Master Entry Point (Dual-Core FreeRTOS)
 * Core 0: Optical Perception & Interleaved Multiplexer Scheduler
 * Core 1: Resonant Tactile Haptic Engine & Cadence Modulator
 * 
 * Team Techtonics - Vishwakarma Awards 2026-27
 * Theme 2: Assistive Solutions (EnAble India), IIT Indore
 */

#include <Arduino.h>
#include "sensor_scheduler.h"
#include "haptic_engine.h"
#include "power_manager.h"

SensorScheduler sensors;
HapticEngine haptics;
PowerManager power;

TaskHandle_t TaskCore0Handle;
TaskHandle_t TaskCore1Handle;

// Shared Queue / Buffer
SensorMeasurement sharedMeasurements[NUM_SENSORS];
portMUX_TYPE sharedMux = portMUX_INITIALIZER_UNLOCKED;

void TaskCore0_SensorEngine(void *pvParameters) {
    sensors.begin(Wire, 1, 2);
    for (;;) {
        sensors.updateInterleavedFiring();
        
        portENTER_CRITICAL(&sharedMux);
        sensors.getAllMeasurements(sharedMeasurements);
        portEXIT_CRITICAL(&sharedMux);
        
        vTaskDelay(pdMS_TO_TICKS(1)); // Yield to FreeRTOS
    }
}

void TaskCore1_HapticEngine(void *pvParameters) {
    haptics.begin(Wire1, 15, 16);
    power.begin(3);
    
    // Startup Self-Test
    haptics.triggerZeroSightSelfTest();
    
    SensorMeasurement localData[NUM_SENSORS];
    
    for (;;) {
        bool moving = power.isUserMoving();
        power.checkPowerState();
        
        portENTER_CRITICAL(&sharedMux);
        memcpy(localData, sharedMeasurements, sizeof(sharedMeasurements));
        portEXIT_CRITICAL(&sharedMux);
        
        // Update all 8 radial haptic nodes
        for (int i = 0; i < NUM_SENSORS; i++) {
            haptics.updateCadence(i, localData[i].distance_mm, moving);
        }
        
        vTaskDelay(pdMS_TO_TICKS(5)); // Hard real-time cycle (<15ms latency)
    }
}

void setup() {
    Serial.begin(115200);
    Serial.println("====================================================");
    Serial.println(" SPATIAL-SENSE: 360 Wearable Haptic-Sonar Waistband ");
    Serial.println(" Team Techtonics - Vishwakarma Awards 2026-27       ");
    Serial.println("====================================================");

    // Pin core tasks
    xTaskCreatePinnedToCore(
        TaskCore0_SensorEngine, "SensorEngine", 4096, NULL, 2, &TaskCore0Handle, 0
    );
    xTaskCreatePinnedToCore(
        TaskCore1_HapticEngine, "HapticEngine", 4096, NULL, 2, &TaskCore1Handle, 1
    );
}

void loop() {
    // Empty; FreeRTOS handles execution on Core 0 and Core 1
    vTaskDelay(pdMS_TO_TICKS(1000));
}
