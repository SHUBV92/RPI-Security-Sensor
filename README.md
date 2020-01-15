# RPi Security Sensor
## Makers October 2019 Cohort Final Project

A home security system, using a Raspberry Pi  with a motion sensor, 2 LED lights, a buzzer, and a camera. Upon detecting motion, a picture is taken, LED lights change from blue to red, and the buzzer beeps. The image is then sent to a hosted website. A notification is also sent to your phone, including a link to the picture's URL.

### Setting up Ruby on Rails:
- Clone the project
- Run 'bundle install'
- Run 'db:create'
- Run 'db:migrate'
- Run 'rspec'

### Setting up hardware:
- List of components:
  - Raspberry Pi (any model with wifi can be used)
  - Breadboard
  - PiCamera
  - Motion Sensor (set to pin 17)
  - 1x Red LED (set to pin 18)
  - 1x Blue LED (set to pin 24)
  - 1x Buzzer (set to pin 22)
  - 2x Resistors
  - 9x m/f Jumper Wires
  - 1x m/m Jumper Wire
*See images below for further setup details*

### APIs used
- IFTTT with PushOver

### Framework information
- Python version 2.7.9
- Rails version 5.1.5
- Ruby gems - see Gemfile
- Python libraries: gpiozero, picamera, requests
- Python testing in Unittest
- Ruby testing in Rspec
- Website testing using Capybara
- Build tested with Travis CI

### Setup images

! Insert images from Michael

! Insert diagram from https://github.com/CamJam-EduKit/EduKit2/blob/master/CamJam%20Edukit%202%20-%20RPi.GPIO/CamJam%20EduKit%202%20-%20Sensors%20Worksheet%205%20(RPi.GPIO)%20-%20Movement.pdf
