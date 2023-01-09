# TempSensor
This is used to connect a temperature sensor from your computer serial port. 

This code assumes that the temperature sensor is sending temperature readings as ASCII strings, terminated with a newline character, and that it can be controlled by sending a '1' or '0' character over the COM port to turn the cooling system on or off, respectively. 
You may need to modify the code depending on the specific protocol used by your temperature sensor.
