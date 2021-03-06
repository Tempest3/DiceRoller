# DiceRoller
This software was written for a Raspberry Pi Model B Rev2. It implements a linear congruency generator to display pseudo-random numbers on a two-digit 7-segment display connected via GPIO pins.

## Requirements
- RPIO library

## Setup
- In “/etc/xdg/lxsession/LXDE-pi/autostart”, add a line to run auto_run.sh. This will launch the LCG script 10 seconds after the user profile is loaded (enabling headless operation).

## Media
- Wiring Diagram for 7-Segment Display:

![wiring diagram](https://user-images.githubusercontent.com/4445235/71755396-641f6400-2e58-11ea-84f5-9122bedf41e4.JPG)

- Video of Final Product:

[final demo](https://drive.google.com/open?id=1FjndLlurGS9un6JL50Kte9yvLXEP8IGG)