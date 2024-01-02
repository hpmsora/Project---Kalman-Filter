################################
#
# Won Yong Ha
#
# VirtualData.py
#
# Create: Dec 12 2023
#
################################

import random as rd
import pandas as pd

class VirtualData:

	def IMUData(self):
		# Return virtual IMU data
		print(rd.random())

		return 0

	def readData(self, _fileName: str):
		try:
			pd.read_csv('/data/' + _fileName)
			return pd.read_csv('/data/' + _fileName)
		except:
			return "error"
