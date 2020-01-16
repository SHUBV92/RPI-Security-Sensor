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
- IFTTT with Slack

### Framework information
- Python version 2.7.9
- Rails version 5.1.5
- Ruby gems - see Gemfile
- Python libraries: gpiozero, picamera, requests
- Python testing in Unittest
- Ruby testing in Rspec
- Website testing using Capybara
- Build tested with Travis CI

### Testing information for Raspberry Pi
There are two tests for the Python code using Unittest. However we discovered that in order test that the hardware is active after it picks up motion we would need to manually stub out each piece of hardware. Instead, it was decided to add two different colour LEDs and a buzzer in order to test the activation. The blue light is on while the motion sensor waits and the red light and buzzer turn on when motion is detected. The blue light turns back on once the photo is taken and the post requests are sent to the website and to IFTTT.

### Setup images
Hardware setup
![Hardware Setup](https://github.com/SHUBV92/RPI-Security-Sensor/blob/master/setupPhotos/Screenshot%202020-01-16%20at%2014.24.11.png =300x220)

Image taken from [The Cambridge Raspberry Jam GitHub](https://github.com/CamJam-EduKit/EduKit2) with thanks.
