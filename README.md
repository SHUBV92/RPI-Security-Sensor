# Security Sensor
## Makers October 2019 Cohort Final Project

A home security system, using a Raspberry Pi, motion sensor, and camera. Upon detecting motion, a picture is taken and sent to a hosted website. A notification is also sent to your phone, including a link to the picture URL.

### Getting Started
- clone the project
- build the hardware (see below for instructions)
- set up the APIs
- run the tests
- visit the website & create an account

### How to set up the motion sensor and camera
- list of components:
  - Raspberry Pi (any model with wifi can be used)
  - PIR Sensor on pin 4
  - PiCamera
  - female-to-female jumper wires
- how to set up the motion sensor
- [Link to camera setup] (https://github.com/CamJam-EduKit/EduKit2/blob/master/CamJam%20Edukit%202%20-%20RPi.GPIO/CamJam%20EduKit%202%20-%20Sensors%20Worksheet%205%20(RPi.GPIO)%20-%20Movement.pdf)

### APIs used
- IFTTT with PushOver

### Framework information
- python version 2.7.9
- rails version 5.1.5
- Ruby gems - see Gemfile
- python libraries: gpiozero, picamera, requests
- Python testing in Unittest, Ruby testing in Rspec, website testing using Capybara
