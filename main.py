import serial
import os

import time
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user="thijs",
    passwd="",
    database="communication"
)

if __name__ == '__main__':
    port = serial.Serial("/dev/ttyUSB0", baudrate="9600", timeout=3.0)

    mycursor = mydb.cursor()

    while True:
        mycursor.execute("SELECT * FROM led;")

        for x in mycursor:
            print(x[1])

        if x[1] == "aan":
            print(x[1])
            port.write(bytes("l1", "utf-8"))
        else:
            port.write(bytes("l0", "utf-8"))

        rcv = port.readline().decode('utf-8').rstrip()

        if(rcv == "b"):
            print("yes")
            os.system("python update.py")

        time.sleep(1)
        mydb.commit()

    mydb.close()