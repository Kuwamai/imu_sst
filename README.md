# imu_sst
IMUで加速度計測して変化検知
## 使い方
* 手頃なIMUをパブリッシュするパッケージを用意
* 確認

```
$ rostopic list 
/imu/data_raw
```

* このリポジトリを持ってくる

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Kuwamai/imu_sst.git
$ cd ~/catkin_ws/
$ catkin_make
```

* rosrunで起動(特異スペクトル変換のみ)

```
$ rosrun imu_sst imu_sst.py
```

* roslaunchで起動(異常度をブラウザへ配信)

```
$ roslaunch imu_sst imu_sst_server.launch
```

ブラウザでアクセス

```
http://<ip_address>:8000
```
