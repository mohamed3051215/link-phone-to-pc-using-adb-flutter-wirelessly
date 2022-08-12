import os


def check_device_connected(command):

    if "List of devices attached" == command:
        return False
    else:
        return True


def get_number_of_devices(command):
    return len(command.split('\n')) - 3


def get_device_name(command):
    return command.split('\n')[1].split('\t')[0]


def get_devices_name(command):
    lines = command.split('\n')
    devices = []
    for line in lines:
        if line != '' and "List of" not in line:
            devices.append(line.split('\t')[0])
    return devices


def ask_for_input(DEVICE_NAMES):
    try:
        device = int(input("Enter the device number: "))
        if device > len(DEVICE_NAMES):
            return ask_for_input()
        return device
    except:
        print("Invalid input")
        return ask_for_input()


def disconnect():
    os.popen('adb disconnect')
