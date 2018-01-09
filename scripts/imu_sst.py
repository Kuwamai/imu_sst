#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
from sensor_msgs.msg import Imu

class Sst:
	def __init__(self):
		self._sst = rospy.Subscriber("imu/data_raw", Imu, self.imu_callback)

		self.M = 5  # 窓幅
		self.n = 3  # trajectory matrixの列数
		self.r = 2  # trajectory matrixのパターン数
		self.k = 3  # test matrixの列数
		self.m = 2  # test matrixのパターン数
		self.L = 3  # ラグ

		#self.X = np.zeros(self.M)
		#self.Z = np.zeros(self.M)
		self.data = np.zeros((1, self.L + self.k + self.M - 1))

	def imu_callback(self, message):
		accel = message.linear_acceleration
		self.data = np.append(self.data, np.array([[accel.z]]), axis=1)
		self.data = np.delete(self.data, 0, axis=1)

		self.X = np.empty((0, self.M))
		for i in range(self.n):
			self.X = np.append(self.X, self.data[0 : 1, i : i + self.M], axis=0)

		self.Z = np.empty((0, self.M))
		for i in range(self.k):
			self.Z = np.append(self.Z, self.data[0 : 1, i + self.L : i + self.L + self.M], axis=0)
		
		print self.X

if __name__ == '__main__':
	rospy.init_node('imu_sst')
	sst = Sst()
	rospy.spin()
