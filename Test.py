################################
#
# Won Yong Ha
#
# Test.py
#
# Create: Dec 12 2023
#
################################

from VirtualData import *
import pandas as pd

def main():
    IMU_virtual_data_test()

def IMU_virtual_data_test():
    VD = VirtualData()

    fileName = 'imu_sensor_data.csv'

    VD.IMUData()

    virtualData = VD.readData(fileName)
    print(virtualData)
    print("AA")

if __name__ == "__main__":
    main()