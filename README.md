# Raspberry Pi Ultrasonic Distance Sensor Projects

This repository contains two small Raspberry Pi projects using an ultrasonic distance sensor.  
The projects demonstrate how open source tools can be used in mechatronics applications.  

---

## Projects

### 1. Distance → Buzzer Trigger
- Measures distance with an ultrasonic sensor.  
- If an object is closer than a threshold (default 20 cm), the buzzer activates.  
- Otherwise, the buzzer stays silent.  

Run with:  
`python buzzer.py`

---

### 2. Distance Zones → LED Control
- Distance less than 10 cm → Red LED glows.  
- Distance between 10–30 cm → White LED glows.  
- Distance greater than 30 cm → Green LED glows.  
- If no object is detected, all LEDs remain off.  

Run with:  
`python leds.py`

---

## Hardware Setup
- **Ultrasonic Sensor (HC-SR04)**  
  - TRIG → GPIO 23  
  - ECHO → GPIO 24  

- **Buzzer**  
  - Signal → GPIO 18  

- **LEDs**  
  - Red → GPIO 17  
  - White → GPIO 27  
  - Green → GPIO 22  

Use resistors in series with LEDs to protect them.  

---

## Requirements
- Raspberry Pi (any model with GPIO support)  
- Python 3  
- RPi.GPIO library  

Install the library:  
`pip install RPi.GPIO`

---

## Usage
1. Clone this repository to your Raspberry Pi.  
2. Wire up the components as described above.  
3. Run the scripts using:  
   - `python buzzer.py`  
   - `python leds.py`  
4. Stop with `Ctrl+C` when finished.  

---

## Notes
- Adjust the distance thresholds inside the code to fit your setup.  
- Sensor accuracy depends on wiring and environment.  
