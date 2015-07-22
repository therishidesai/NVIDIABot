import serial
import time
ser = serial.Serial('/dev/ttyACM2')
#while(True):
data = [1,0, 2, 3]
str1=""
for i in range(4):
    str1+=`data[i]`
    str1+=","
print str1
ser.write(str1)
#time.sleep(2)
print ser.bytesize
print ser.read(2)
    
