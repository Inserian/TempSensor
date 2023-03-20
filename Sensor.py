import serial
import time
import tkinter as tk
from tkinter import messagebox
from threading import Thread

def read_and_control_temperature(com_port, baud_rate, threshold, read_interval):
    try:
        with serial.Serial(com_port, baud_rate) as ser:
            while True:
                # Read a temperature reading from the sensor
                temperature = ser.readline()
                # Convert the temperature reading to a float
                temperature_value = float(temperature.strip())
                temperature_label_var.set(f'Temperature: {temperature_value}')
                
                # If the temperature is above the threshold, turn on the cooling system
                if temperature_value > threshold:
                    ser.write(b'1')
                    system_state_label_var.set('Cooling system activated')
                else:
                    # Otherwise, turn off the cooling system
                    ser.write(b'0')
                    system_state_label_var.set('Cooling system deactivated')
                
                # Wait for the specified read interval before reading the next value
                time.sleep(read_interval)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def start_temperature_monitor():
    COM_PORT = com_port_entry.get()
    BAUD_RATE = int(baud_rate_entry.get())
    THRESHOLD = float(threshold_entry.get())
    READ_INTERVAL = float(read_interval_entry.get())

    temperature_thread = Thread(target=read_and_control_temperature, args=(COM_PORT, BAUD_RATE, THRESHOLD, READ_INTERVAL), daemon=True)
    temperature_thread.start()

# Create the tkinter GUI window
root = tk.Tk()
root.title("Temperature Monitor")

com_port_label = tk.Label(root, text="COM Port:")
com_port_label.grid(row=0, column=0, sticky="e")
com_port_entry = tk.Entry(root)
com_port_entry.grid(row=0, column=1)
com_port_entry.insert(0, "COM3")

baud_rate_label = tk.Label(root, text="Baud Rate:")
baud_rate_label.grid(row=1, column=0, sticky="e")
baud_rate_entry = tk.Entry(root)
baud_rate_entry.grid(row=1, column=1)
baud_rate_entry.insert(0, "9600")

threshold_label = tk.Label(root, text="Temperature Threshold:")
threshold_label.grid(row=2, column=0, sticky="e")
threshold_entry = tk.Entry(root)
threshold_entry.grid(row=2, column=1)
threshold_entry.insert(0, "25")

read_interval_label = tk.Label(root, text="Read Interval (s):")
read_interval_label.grid(row=3, column=0, sticky="e")
read_interval_entry = tk.Entry(root)
read_interval_entry.grid(row=3, column=1)
read_interval_entry.insert(0, "2")

start_button = tk.Button(root, text="Start", command=start_temperature_monitor)
start_button.grid(row=4, column=0, columnspan=2)

temperature_label_var = tk.StringVar()
temperature_label = tk.Label(root, textvariable=temperature_label_var)
temperature_label.grid(row=5, column=0, columnspan=2)

system_state_label_var = tk.StringVar()
system_state_label = tk.Label(root, textvariable=system_state_label_var)
system_state_label.grid(row=6, column=0, columnspan=2)

# Run the tkinter GUI main loop
root.mainloop()
