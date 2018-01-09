# imu_sst
IMUで加速度計測して変化検知
## 使い方
1. 手頃なIMUの値だすパッケージを用意
1. 確認

  ```
  $ rostopic list 
  /imu/data_raw
  ```

1. このリポジトリを持ってくる

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Kuwamai/imu_sst.git
$ cd ~/catkin_ws/
$ catkin_make
```

1. rosrunで起動

```
rosrun imu_sst imu_sst.py
```

