# imu_sst
## Description
* IMUが取得したデータをsubscribeし、singular spectrum transformationして変化度をpublishする
* 動画はこんな感じ
## Requirements
* Raspberry Pi3
* IMU
* Ubuntu16.04
* ROS kinetic
* rosbridge_server
## Installation
* 手頃なIMUをパブリッシュするパッケージを実行
* 以下のコマンドで`/imu/data_raw`があることを確認

```
$ rostopic list 
/imu/data_raw
```

* このリポジトリをcloneする
* 以下のコマンドを実行

```
$ cd ~/catkin_ws/src/
$ git clone https://github.com/Kuwamai/imu_sst.git
$ cd ~/catkin_ws/
$ catkin_make
```

## Usage

* roslaunchで起動

```
$ roslaunch imu_sst imu_sst_server.launch
```

* ブラウザでアクセス

```
http://<ip_address>:8000
```

## License
This repository is licensed under the BSD license, see [LICENSE](./LICENSE).
