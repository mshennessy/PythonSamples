# 3704 Receive data from a micro:bit via a serial port
# G Hennessy CUS
# Your MicroBit must be connected throuh your USB port
# You should have code downloaded onto it using the "Serial" feature (advanced)
# This code assumes you have "serial redirect to USB" in the start block
# and "serial write line" in a forever loop (preferably with a 5 sec delay)

# Comment out this code once you have run it once to identify the correct port
# Look for the one that says USB and change ser.port to this value below
import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)

# Set your python code up to be able to collect data over a serial link
import serial
ser = serial.Serial()
ser.baudrate = 115200 # This is the micro:bit baudrate, don't change
ser.port = 'COM3' #This will differ on different systems - use code above to find correct port

ser.open()
# Open for appending 'a' when you are collecting real data
# Open for writing 'w' when you are in test mode
file = open("temperatures_from_microbit.csv",'w') 
# use while True: for forever ...
# but it's easier to set a limit for testing
countData = 0
gatheredData=[]
while (countData < 50):
    # Fancier readline
    #data = str(ser.readline().decode().strip())
    # Basic readline
    data = str(ser.readline())
    print ("Received >>",data,"<<")
    data = data.replace("b","")  # strip out unwanted characters 
    data = data.replace(" ","")
    data = data.replace("'","")
    #separating \r and \n seems to work better
    #\r is carriage return and \n is newline
    data = data.replace("\\r","") # strip out line feeds
    data = data.replace("\\n","")
    print ("Processed data >>",data,"<<\n")
    gatheredData.append(data)
    file.write(data+"\n")
    countData += 1
print ("Finished")
file.close()

for i in gatheredData:
    print(i)
    
