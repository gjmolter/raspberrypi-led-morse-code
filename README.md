# GM_RPiMorseCodeLEDBlink
Python script that converts text to Morse Code and blink a LED light using Raspberry Pi's GPIO

#### Just a small project I've created as a Python exercise. ####


#### CRAFTING THE CIRCUIT
To build the circuit you will need 
- 2 Jumper Cables
- 1 BreadBoard (You can use duct tape instead)
- 1 220 ohms resistor
- 1 LED

Electricity Path:

Pin 18 (GPIO 24) → Jumper → BreadBoard → Resistor → LED → Breadboard → Jumper → Pin 6 (Ground)

If you don't have a breadboard, you should be fine taping everything.

#### HOW TO RUN IT
Just run the `ledblinkRaspberry.py` file with superuser privileges (root).
(You obviously need to have Python installed).

![GPIO MAP](http://2.bp.blogspot.com/-fLqGQ-E-EXA/UD0XdnCVOrI/AAAAAAAAAF8/c19SPUGftjU/s1600/Raspberry-Pi-GPIO-Layout.png)
