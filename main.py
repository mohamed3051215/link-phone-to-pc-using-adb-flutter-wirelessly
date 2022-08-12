from utils import *
import os
import time
NUMBER_OF_DEVICES = 0   # number of devices connected
DEVICE_NAMES = []
DEVICES_STATES = dict()
DEVICES_IPS = dict()

disconnect()
adb_devices_cmd = os.popen('adb devices').read()
if check_device_connected(adb_devices_cmd) == False:
    print("No Device found please connect you device with USB and enable USB Debugging from settings")
    time.sleep(2)
    exit()
print("Device found")
NUMBER_OF_DEVICES = get_number_of_devices(adb_devices_cmd)
print("Number of devices connected: " + str(NUMBER_OF_DEVICES))

if(NUMBER_OF_DEVICES == 1):
    ip_command = os.popen('adb shell ip rout').read()  # get ip route
    ip = ip_command.split(' ')[-1]
    # start tcpip server on 5555
    tcpip_command = os.popen("adb tcpip 5555").read()
    print("TCPIP DONE SUCCESSFULLY : " + tcpip_command)
    connect_command = os.popen(
        "adb connect " + ip + ":5555").read()  # connect to device
    print("CONNECT DONE SUCCESSFULLY : " + connect_command)
    time.sleep(2)
    exit()

# if more than one device connected
DEVICE_NAMES = get_devices_name(adb_devices_cmd)

for index, device in enumerate(DEVICE_NAMES):
    state_command = os.popen('adb -s ' + device + ' get-state').read()
    DEVICES_STATES[device] = state_command
    DEVICES_IPS[device] = os.popen(
        'adb -s ' + device + ' shell ip rout').read().split(' ')[-1]
print("GOT DEVICE NAMES AND IPS\n\n")

print("Multiple devices connected, Please choose one of the following devices: ")
for index, device in enumerate(DEVICE_NAMES):
    print(str(index + 1) + ": " + device + " " +
          DEVICES_STATES[device] + " " + DEVICES_IPS[device])

device_index = ask_for_input(DEVICE_NAMES=DEVICE_NAMES)
device = DEVICE_NAMES[device_index - 1]
ip = DEVICES_IPS[device]
# start tcpip server on 5555
print(os.popen("adb -s " + device + " tcpip 5555").read())
print(os.popen("adb -s " + device + " connect " +
      ip + ":5555").read())  # connect to device

print("Connected to " + device + " " +
      DEVICES_STATES[device] + " " + DEVICES_IPS[device])
time.sleep(2)
