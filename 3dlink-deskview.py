import serial,serial.tools.list_ports
import time
import requests
import os

os.system('cls')
os.system('color c')
os.system('mode con: cols=64 lines=49')

print("""
   _____ ____  __    _       __  
  |__  // __ \/ /   (_)___  / /__
   /_ </ / / / /   / / __ \/ //_/
 ___/ / /_/ / /___/ / / / / ,<   
/____/_____/_____/_/_/ /_/_/|_|  
DesktopViewer - Nafaneel 
""")
print()
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("CONFIGURE SETTINGS:")
print()
myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
print(myports)
print()
ser = serial.Serial('COM5')
time.sleep(1)
print("SELECTED PORT:")
  # open serial port
print(ser.name)         # check which port was really used

web = "https://3dlink-deskviewer.nafaneel.repl.co"
#web = "http://192.168.0.42:5000"
print()
print("DATA LINK:")
print(web)
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
print("""
nozzle       = int(0-240) - Current Nozzle Temp
nozzleLimit1 = int(0-240) - Nozzle Temp Limit
bed          = int(0-110) - Current Bed Temp
bedLimit     = int(0-110) - Bed Temp Limit
temp         = int(0-100) - Enclosure Temp
humid        = int(0-100) - Enclosure Humidity
headPos      = True/False - True = Home position
printStat    = True/False - True = Printing 
material     = "ABS"
cooling      = True/False - True = Cooling Enabled
finish       = "00:00:00"
total        = "00:00:00"
""")
print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")

ser.write(b'???????????????????????????????????????????????????????????????????') 



def loopTest():

    for i in range(5):
        ser.write(b'000,240-000,110-00.00-00.00-False-False-ABS-False-00:00:00-00:00:00')
        time.sleep(2)

    for i in range(5):
        ser.write(b'240,240-110,110-36.00-57.00-True -True -PLA-True -00:00:00-00:00:00')
        time.sleep(2)  

    for i in range(5):
        ser.write(b'230,240-110,110-36.00-57.00-True -True -PLA-True -00:00:00-00:00:00')
        time.sleep(2) 

    for i in range(3):
        ser.write(b'240,240-100,110-36.00-57.00-False-False-ABS-False-00:00:00-00:00:00')
        time.sleep(2)

    for i in range(5):
        ser.write(b'000,240-000,110-36.00-57.00-False-False-ABS-False-00:00:00-00:00:00')
        time.sleep(2)

    #loopTest()


#loopTest()

#inputText = str("000,000,00.00,00.00")
#b = bytes(inputText, 'utf-8')


def test():
    r = requests.get(web)
    b = bytes(str(r.text), 'utf-8')
    ser.write(b)
    time.sleep(3)
    test()
test()




    
#ser.close()       
