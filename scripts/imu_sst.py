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

		self.X = np.array([])
		self.Z = np.array([])

	def imu_callback(self, message):
		accel = message.linear_acceleration
		print accel.z

# def recv_imu(message):
#	accel = message.linear_acceleration
#	omega = message.angular_velocity
#	print accel.z
	
if __name__ == '__main__':
	rospy.init_node('imu_sst')
	sst = Sst()
	rospy.spin()
