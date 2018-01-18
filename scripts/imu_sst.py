#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import numpy as np
from sensor_msgs.msg import Imu
from std_msgs.msg import Float64

class Sst:
	def __init__(self):
		self._sub = rospy.Subscriber("imu/data_raw", Imu, self.imu_callback)
		self._pub = rospy.Publisher("anomaly_score", Float64, queue_size=10)

		self.M = 55555  # 窓幅
		self.n = 3  # trajectory matrixの列数
		self.r = 2  # trajectory matrixのパターン数
		self.k = 3  # test matrixの列数
		self.m = 2  # test matrixのパターン数
		self.L = 3  # ラグ

		self.data = np.zeros((self.L + self.k + self.M - 1, 1))

	def imu_callback(self, message):
		accel = message.linear_acceleration
		self.data = np.append(self.data, np.array([[accel.z]]), axis=0)
		self.data = np.delete(self.data, 0, axis=0)

		X = np.empty((self.M, 0))
		for i in range(self.n):
			X = np.append(X, self.data[i : i + self.M, 0 : 1], axis=1)

		Z = np.empty((self.M, 0))
		for i in range(self.k):
			Z = np.append(Z, self.data[i + self.L : i + self.L + self.M, 0 : 1], axis=1)
		
		U1, S1, V1  = np.linalg.svd(X, full_matrices=False)
		U2, S2, V2  = np.linalg.svd(Z, full_matrices=False)

		U_r  = U1[:, :self.r]
		Q_m  = U2[:, :self.m]

		s = np.linalg.svd(U_r.T.dot(Q_m), full_matrices=False, compute_uv=False)
		anomaly_score = 1 - s[0]

		self._pub.publish(anomaly_score)

if __name__ == '__main__':
	rospy.init_node('imu_sst')
	sst = Sst()
	rospy.spin()
