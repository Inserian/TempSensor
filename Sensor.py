import serial

# Set the COM port number and baud rate
COM_PORT = 'COM3'
BAUD_RATE = 9600

# Connect to the COM port
with serial.Serial(COM_PORT, BAUD_RATE) as ser:
    # Read a temperature reading from the sensor
    temperature = ser.readline()
    print(f'Temperature: {temperature}')
    
    # Set the temperature threshold
    threshold = 25
    
    # If the temperature is above the threshold, turn on the cooling system
    if temperature > threshold:
        ser.write(b'1')
        print('Cooling system activated')
    else:
        # Otherwise, turn off the cooling system
        ser.write(b'0')
        print('Cooling system deactivated')
